import os
import json
import re
import sys

ROOT = "."
REQUIRED_FILES = ["description.md", "io.json", "meta.json", "starter.py"]
REQUIRED_META_FIELDS = ["title", "name", "difficulty", "author", "category"]

total_failures = 0
broken_dirs = []

def print_error(folder, msg):
    global total_failures
    print(f"{folder}: {msg}")
    total_failures += 1

for folder in os.listdir(ROOT):
    #skips the .git directory
    if folder.startswith("."):
        continue

    path = os.path.join(ROOT, folder)
    if not os.path.isdir(path):
        continue

    has_issue = False

    # Checks required files exist and are not empty
    for file in REQUIRED_FILES:
        file_path = os.path.join(path, file)
        if not os.path.isfile(file_path):
            print_error(folder, f"Missing file: {file}")
            has_issue = True
        elif os.path.getsize(file_path) == 0:
            print_error(folder, f"{file} exists but is empty.")
            has_issue = True
        
    # Check io.json is valid JSON and not empty    
    io_path = os.path.join(path, "io.json")
    if os.path.isfile(io_path) and os.path.getsize(io_path) > 0:
        try:
            with open(io_path) as f:
                io_data = json.load(f)
            if not io_data:
                print_error(folder, "io.json is valid but contains no test cases.")
                has_issue = True
        except Exception as e:
            print_error(folder, f"io.json is not valid JSON: {e}")
            has_issue = True
    
    # Check meta.json is valid and has required fields
    meta_path = os.path.join(path, "meta.json")
    meta = {}
    if os.path.isfile(meta_path) and os.path.getsize(meta_path) > 0:
        try:
            with open(meta_path) as f:
                meta = json.load(f)
            for field in REQUIRED_META_FIELDS:
                if field not in meta:
                    print_error(folder, f"meta.json missing field: {field}")
                    has_issue = True
        except Exception as e:
            print_error(folder, f"meta.json is not valid JSON: {e}")
            has_issue = True
        
    # Validate function name in starter.py    
    starter_path = os.path.join(path, "starter.py")
    if meta.get("name") and os.path.isfile(starter_path) and os.path.getsize(starter_path) > 0:
        try:
            with open(starter_path) as f:
                content = f.read()
            pattern = rf"def\s+{re.escape(meta['name'])}\s*\("
            if not re.search(pattern, content):
                print_error(folder, f"starter.py does not define the expected function: {meta['name']}()")
                has_issue = True
        except Exception as e:
            print_error(folder, f"Error reading starter.py: {e}")
            has_issue = True
    
    if has_issue:
        broken_dirs.append(folder)
        print(f"{folder} failed validation. \n")

if broken_dirs:
    print(f"{len(broken_dirs)} problem folder(s) failed validation:")
    for d in broken_dirs:
        print(f"    - {d}")
    sys.exit(1)
else:
    print("All problem folders passed validation.")
    sys.exit(0)