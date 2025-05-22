#!/usr/bin/env python3
import os
import shutil
import json
import glob
import argparse

def patch_meta(directory, question_types, name_override=None):
    meta_path = os.path.join(directory, 'meta.json')
    if not os.path.isfile(meta_path):
        print(f"Warning: meta.json not found in {directory}")
        return
    with open(meta_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # Update question_type
    data['question_type'] = question_types
    # Optionally override the name field
    if name_override:
        data['name'] = name_override
    with open(meta_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Updated meta.json in {directory}: question_type={question_types}" + \
          (f", name={name_override}" if name_override else ""))

def split_dirs(root_dir):
    for name in os.listdir(root_dir):
        orig_dir = os.path.join(root_dir, name)
        # Skip non-directories and already-handled mutation dirs
        if not os.path.isdir(orig_dir) or name.endswith('-mutation'):
            continue
        # Detect mutation files in the directory
        mutations = glob.glob(os.path.join(orig_dir, 'mutation_*.py'))
        if not mutations:
            continue
        # Name for the mutation directory
        mut_name = f"{name}-mutation"
        mut_dir = os.path.join(root_dir, mut_name)
        # Create mutation directory copy if missing
        if os.path.exists(mut_dir):
            print(f"Skipping creation, {mut_dir} already exists")
        else:
            shutil.copytree(orig_dir, mut_dir)
            # Remove the starter.py from the mutation directory
            starter = os.path.join(mut_dir, 'starter.py')
            if os.path.isfile(starter):
                os.remove(starter)
            # Update its meta.json (include name override)
            override_name = mut_name.replace('-', '_')
            patch_meta(mut_dir, ['mutation'], override_name)
        # Clean the original directory: remove mutation & solution files
        for pattern in ['mutation_*.py', 'solution*.py']:
            for fpath in glob.glob(os.path.join(orig_dir, pattern)):
                os.remove(fpath)
                print(f"Removed {fpath}")
        # Update original directory's meta.json for coding
        patch_meta(orig_dir, ['coding'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Split coding and mutation directories into separate folders.'
    )
    parser.add_argument(
        'root', nargs='?', default='.',
        help='Root directory containing problem folders'
    )
    args = parser.parse_args()
    split_dirs(args.root)
