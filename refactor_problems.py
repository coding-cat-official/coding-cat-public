#!/usr/bin/env python3
import os
import json
import shutil
import re

def slugify(name: str) -> str:
    """
    Convert a category name into a filesystem-safe directory name:
    lowercase, non-alphanumerics → underscores, no leading/trailing underscores.
    """
    slug = re.sub(r'\W+', '_', name.lower()).strip('_')
    return slug or "uncategorized"

def main():
    root = os.getcwd()

    # Names of special buckets
    SPECIAL_DIRS = {"mutation", "haystack"}

    # 1) Look at every entry in the root
    for entry in os.listdir(root):
        entry_path = os.path.join(root, entry)
        # Only consider directories
        if not os.path.isdir(entry_path):
            continue
        # Skip the special dirs (so you don’t re-process them once created)
        if entry in SPECIAL_DIRS:
            continue

        # 2) Check for a meta.json inside
        meta_file = os.path.join(entry_path, "meta.json")
        if not os.path.isfile(meta_file):
            continue

        # 3) Load its metadata
        with open(meta_file, "r", encoding="utf-8") as f:
            meta = json.load(f)

        qtypes = meta.get("question_type", [])
        category = meta.get("category", "uncategorized")

        # 4) Decide destination folder
        if "mutation" in qtypes:
            dest_folder = "mutation"
        elif "haystack" in qtypes:
            dest_folder = "haystack"
        else:
            dest_folder = slugify(category)

        dest_path = os.path.join(root, dest_folder)
        os.makedirs(dest_path, exist_ok=True)

        # 5) Move the entire problem directory under the chosen folder
        shutil.move(entry_path, os.path.join(dest_path, entry))
        print(f"Moved '{entry}' → '{dest_folder}/'")

if __name__ == "__main__":
    main()
