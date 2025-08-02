import os

def list_all_files(base_folder):
    print(f"\n📁 Listing all files in '{base_folder}' and its subfolders:\n")
    for root, dirs, files in os.walk(base_folder):
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), base_folder)
            print(rel_path)

if __name__ == "__main__":
    folder_name = r"D:\Code Generation\Financial Data Parser\financial-data-parser"
    list_all_files(folder_name)
