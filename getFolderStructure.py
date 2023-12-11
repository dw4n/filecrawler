import os

def list_files(startpath):
    output_file = "root-structure-tree.txt"

    with open(output_file, "w") as f:
        for root, dirs, files in os.walk(startpath):
            # Skip .git directories and their contents
            if '.git' in root.split(os.sep):
                continue

            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * level
            f.write('{}{}/\n'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)

            for file in files:
                # Skip .gitignore files
                if file == '.gitignore':
                    continue

                f.write('{}{}\n'.format(subindent, file))

if __name__ == "__main__":
    list_files('.')