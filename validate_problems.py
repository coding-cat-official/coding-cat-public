#!/usr/bin/env python3
import os
import json
import re
import sys
import glob

ROOT = '.'
# Files common to both types
REQUIRED_COMMON = ['description.md', 'io.json', 'meta.json']
# Meta fields that must always be present
REQUIRED_META_FIELDS = ['title', 'name', 'difficulty', 'author', 'category', 'question_type']

total_failures = 0
broken_dirs = []

def print_error(folder, msg):
    global total_failures
    print(f"{folder}: {msg}")
    total_failures += 1

for folder in os.listdir(ROOT):
    # Skip hidden files/dirs and non-directories
    if folder.startswith('.'):
        continue
    path = os.path.join(ROOT, folder)
    if not os.path.isdir(path):
        continue

    has_issue = False
    # 1. Check common files exist and are non-empty
    for fname in REQUIRED_COMMON:
        fpath = os.path.join(path, fname)
        if not os.path.isfile(fpath):
            print_error(folder, f"Missing file: {fname}")
            has_issue = True
        elif os.path.getsize(fpath) == 0:
            print_error(folder, f"{fname} exists but is empty.")
            has_issue = True

    # 2. Validate io.json
    io_path = os.path.join(path, 'io.json')
    if os.path.isfile(io_path) and os.path.getsize(io_path) > 0:
        try:
            with open(io_path, encoding='utf-8') as f:
                io_data = json.load(f)
            if not io_data:
                print_error(folder, "io.json contains no test cases.")
                has_issue = True
        except Exception as e:
            print_error(folder, f"io.json invalid JSON: {e}")
            has_issue = True

    # 3. Validate meta.json and extract question_type
    meta_path = os.path.join(path, 'meta.json')
    meta = {}
    if os.path.isfile(meta_path) and os.path.getsize(meta_path) > 0:
        try:
            with open(meta_path, encoding='utf-8') as f:
                meta = json.load(f)
            for field in REQUIRED_META_FIELDS:
                if field not in meta:
                    print_error(folder, f"meta.json missing field: {field}")
                    has_issue = True
        except Exception as e:
            print_error(folder, f"meta.json invalid JSON: {e}")
            has_issue = True
    else:
        # meta.json missing or empty handled above
        meta = {}

    qtypes = meta.get('question_type', [])

    # 4. Validate coding directories
    if 'coding' in qtypes:
        # starter.py must exist
        starter_path = os.path.join(path, 'starter.py')
        if not os.path.isfile(starter_path):
            print_error(folder, "Missing starter.py for coding question")
            has_issue = True
        else:
            # Check function name matches meta['name']
            func_name = meta.get('name')
            if func_name:
                try:
                    content = open(starter_path, encoding='utf-8').read()
                    pattern = rf"def\s+{re.escape(func_name)}\s*\("
                    if not re.search(pattern, content):
                        print_error(folder, f"starter.py does not define function {func_name}()")
                        has_issue = True
                except Exception as e:
                    print_error(folder, f"Error reading starter.py: {e}")
                    has_issue = True
        # Should not have mutation files
        muts = glob.glob(os.path.join(path, 'mutation_*.py'))
        if muts:
            print_error(folder, "Coding directory should not contain mutation tests")
            has_issue = True

    # 5. Validate mutation directories
    if 'mutation' in qtypes:
        # solution.py (or solution_*.py) must exist
        sol_files = glob.glob(os.path.join(path, 'solution*.py'))
        if not sol_files:
            print_error(folder, "Missing solution.py for mutation question")
            has_issue = True
        # Must have at least one mutation test
        muts = glob.glob(os.path.join(path, 'mutation_*.py'))
        if not muts:
            print_error(folder, "No mutation_*.py files in mutation question")
            has_issue = True
        # Should not have starter.py
        starter_path = os.path.join(path, 'starter.py')
        if os.path.isfile(starter_path):
            print_error(folder, "Mutation directory should not contain starter.py")
            has_issue = True

    # 6. Validate question_type values
    if not set(qtypes).intersection({'coding', 'mutation'}):
        print_error(folder, "question_type must include 'coding' or 'mutation'")
        has_issue = True
    if 'coding' in qtypes and 'mutation' in qtypes:
        print_error(folder, "question_type should not include both 'coding' and 'mutation'")
        has_issue = True

    if has_issue:
        broken_dirs.append(folder)
        print(f"{folder} failed validation.\n")

# Summary and exit
if broken_dirs:
    print(f"{len(broken_dirs)} problem folder(s) failed validation:")
    for d in broken_dirs:
        print(f"  - {d}")
    sys.exit(1)
else:
    print("All problem folders passed validation.")
    sys.exit(0)
