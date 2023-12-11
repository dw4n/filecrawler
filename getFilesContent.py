import os

excludedFilesExt = [".git", ".vs", ".yml", ".pem", ".example", ".gitignore", ".gitlab-ci.yml", ".env", ".env.example"]
excludedFolders = [".git", "vendor", "scripts", "docs", "deployments", "pkg"]
excludeFiles = ["structured-folders-files-and-contents.txt"]  # Add the filename to exclude
output_file = "structured-folders-files-and-contents.txt"

def list_files_with_content(startpath, excluded_files, output_file):
    visited_paths = set()  # Maintain a set of visited paths to avoid duplicates
    processed_files = set()  # Maintain a set of processed files to avoid reading the same file twice

    with open(output_file, "w") as f:
        for root, dirs, files in os.walk(startpath):
            # Check if the current path has already been visited
            if root in visited_paths:
                continue

            visited_paths.add(root)  # Add the current path to the set of visited paths

            # Create a set of folder names in the current path
            path_folders = set(root.split(os.sep))

            # Check if the set of current path folders intersects with excluded folders
            if any(folder in path_folders for folder in excludedFolders):
                continue  # Skip this root folder

            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * level
            f.write('{}{}/\n'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)

            for file in files:
                # Skip excluded files, Python files, files that have been processed, and files in the excludeFiles list
                if (file in excludedFilesExt or file.endswith('.py') or file in processed_files
                    or file in excludeFiles):
                    continue

                file_path = os.path.join(root, file)
                f.write('{}{}\n'.format(subindent, file))

                try:
                    with open(file_path, "r") as input_file:
                        content = input_file.read()
                        f.write(content + "\n\n")
                    processed_files.add(file)  # Add the processed file to the set
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")

if __name__ == "__main__":
    list_files_with_content('.', excluded_files=excludedFilesExt, output_file=output_file)
