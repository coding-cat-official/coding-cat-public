import os

def prompt_and_write(file_path, prompt_message):
    print(f"> {prompt_message}")
    print("(Paste your input. End with an empty line.)")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    content = "\n".join(lines)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Created {file_path}")

def main():
    problem_name = input("> What is the name of the problem (used for folder, title, and function name)? ").strip()
    folder_name = problem_name.replace(" ", "_").lower()

    os.makedirs(folder_name, exist_ok=True)
    print(f"📁 Created folder: {folder_name}")

    files_and_prompts = [
        ("description.md", "Enter the contents of the description.md"),
        ("io.json", "Enter the content of the io.json"),
        ("meta.json", "Enter the meta.json"),
        ("starter.py", "Enter the starter.py"),
    ]

    for filename, prompt in files_and_prompts:
        full_path = os.path.join(folder_name, filename)
        prompt_and_write(full_path, prompt)

    print("🎉 All files created successfully!")

    again = input("Would you like to create another problem? y/n")
    if again.lower() == "y":
        main()

if __name__ == "__main__":
    main()
