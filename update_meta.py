import os
import json

def update_meta_files(base_path):
    for root, dirs, files in os.walk(base_path):
        if 'meta.json' in files:
            meta_path = os.path.join(root, 'meta.json')
            starter_exists = 'starter.py' in files
            mutation_exists = any(f.startswith('mutation_') and f.endswith('.py') for f in files)

            question_type = []
            if starter_exists:
                question_type.append('coding')
            if mutation_exists:
                question_type.append('mutation')

            if question_type:
                try:
                    with open(meta_path, 'r', encoding='utf-8') as f:
                        meta_data = json.load(f)

                    meta_data['question_type'] = question_type

                    with open(meta_path, 'w', encoding='utf-8') as f:
                        json.dump(meta_data, f, indent=2)
                    
                    print(f"Updated {meta_path} with question_type: {question_type}")
                except Exception as e:
                    print(f"Error updating {meta_path}: {e}")

if __name__ == "__main__":
    base_directory = os.getcwd()
    update_meta_files(base_directory)
