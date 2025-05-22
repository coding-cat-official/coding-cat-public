#!/usr/bin/env python3
import os
import json
import re
import sys
import glob

ROOT = '.'

# special buckets which live at top level
SPECIAL_DIRS = {'mutation', 'haystack'}

# files that every problem directory must have
REQUIRED_COMMON = ['description.md', 'io.json', 'meta.json']

# fields that meta.json must define
REQUIRED_META_FIELDS = [
    'title',
    'name',
    'difficulty',
    'author',
    'category',
    'question_type'
]

# track failures
total_failures = 0
broken = []


def slugify(name: str) -> str:
    """Lowercase, non-alphanumerics → underscores, trim."""
    slug = re.sub(r'\W+', '_', name.strip().lower()).strip('_')
    return slug or 'uncategorized'


def error(path, msg):
    global total_failures
    print(f"[ERROR] {path}: {msg}")
    total_failures += 1


def validate_problem(problem_path, rel_path):
    """
    Validate one problem directory at problem_path.
    rel_path is something like 'list_2_iterating/add-evens'.
    """
    # 1) common files exist & non-empty
    for fn in REQUIRED_COMMON:
        p = os.path.join(problem_path, fn)
        if not os.path.isfile(p):
            error(rel_path, f"missing file {fn}")
        elif os.path.getsize(p) == 0:
            error(rel_path, f"{fn} is empty")

    # 2) io.json is valid JSON and non-empty
    io_p = os.path.join(problem_path, 'io.json')
    if os.path.isfile(io_p):
        try:
            data = json.load(open(io_p, encoding='utf-8'))
            if not data:
                error(rel_path, "io.json contains no test cases")
        except Exception as e:
            error(rel_path, f"io.json invalid JSON: {e}")

    # 3) meta.json presence & fields
    meta = {}
    meta_p = os.path.join(problem_path, 'meta.json')
    if os.path.isfile(meta_p):
        try:
            meta = json.load(open(meta_p, encoding='utf-8'))
            for field in REQUIRED_META_FIELDS:
                if field not in meta:
                    error(rel_path, f"meta.json missing field '{field}'")
        except Exception as e:
            error(rel_path, f"meta.json invalid JSON: {e}")

    qtypes = meta.get('question_type', [])
    name = meta.get('name', '')
    category = meta.get('category', '')

    # 4) check placement
    parent_dir = rel_path.split(os.sep)[0]
    if 'mutation' in qtypes:
        expected = 'mutation'
    elif 'haystack' in qtypes:
        expected = 'haystack'
    else:
        expected = slugify(category)
    if parent_dir != expected:
        error(rel_path, f"in '{parent_dir}' but should be in '{expected}'")

    # 5) coding & haystack questions
    if any(t in qtypes for t in ('coding', 'haystack')):
        # starter.py must exist
        st = os.path.join(problem_path, 'starter.py')
        if not os.path.isfile(st):
            error(rel_path, "missing starter.py for coding/haystack question")
        else:
            # ensure function def matches meta.name
            if name:
                content = open(st, encoding='utf-8').read()
                pat = rf"def\s+{re.escape(name)}\s*\("
                if not re.search(pat, content):
                    error(rel_path, f"starter.py does not define function '{name}()'")
        # should not have mutation files
        muts = glob.glob(os.path.join(problem_path, 'mutation_*.py'))
        if muts:
            error(rel_path, "contains mutation_*.py but is a coding/haystack question")

    # 6) mutation questions
    if 'mutation' in qtypes:
        # need solution*.py
        sols = glob.glob(os.path.join(problem_path, 'solution*.py'))
        if not sols:
            error(rel_path, "missing solution.py for mutation question")
        # need at least one mutation_x.py
        muts = glob.glob(os.path.join(problem_path, 'mutation_*.py'))
        if not muts:
            error(rel_path, "no mutation_*.py files in mutation question")
        # must not have starter.py
        if os.path.isfile(os.path.join(problem_path, 'starter.py')):
            error(rel_path, "contains starter.py but is a mutation question")

    # 7) question_type sanity
    allowed = {'coding', 'mutation', 'haystack'}
    present = set(qtypes) & allowed
    if not present:
        error(rel_path, "question_type must include one of 'coding','mutation','haystack'")
    if len(present) > 1:
        error(rel_path, f"question_type has multiple of {present}; only one allowed")


def main():
    # scan root-level to ensure no stray problem dirs
    for item in os.listdir(ROOT):
        if item.startswith('.') or item in SPECIAL_DIRS:
            continue
        p = os.path.join(ROOT, item)
        if os.path.isdir(p) and os.path.isfile(os.path.join(p, 'meta.json')):
            error(item, "problem folder found at root; must live under a category, 'mutation' or 'haystack'")

    # now scan two levels deep: ROOT/<bucket>/<problem>
    for bucket in os.listdir(ROOT):
        bucket_path = os.path.join(ROOT, bucket)
        if not os.path.isdir(bucket_path) or bucket.startswith('.'):
            continue
        # skip any non-problem container (but allow SPECIAL_DIRS + category slugs)
        # we don't know all categories in advance, so treat any dir as potential container
        for problem in os.listdir(bucket_path):
            problem_path = os.path.join(bucket_path, problem)
            if not os.path.isdir(problem_path):
                continue
            # only care if it's a problem dir (has meta.json)
            if os.path.isfile(os.path.join(problem_path, 'meta.json')):
                rel = os.path.join(bucket, problem)
                validate_problem(problem_path, rel)
    # exit status
    if total_failures:
        print(f"\n{total_failures} validation error(s) found.")
        sys.exit(1)
    else:
        print("All problem directories passed validation.")
        sys.exit(0)


if __name__ == '__main__':
    main()
