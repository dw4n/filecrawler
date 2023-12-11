# filecrawler
A file crawler python function to read all data inside of your folder. Useful to import files and its content to LLM.

## How to run
1. Install Phyton
2. run 
```
py getFilesContent.py
py getFolderStructure.py
```
3. Optional
Type any excluded folder, files, or extensions at the top of it.
```
excludedFilesExt = [".git", ".vs", ".yml", ".pem", ".example", ".gitignore", ".gitlab-ci.yml", ".env", ".env.example"]
excludedFolders = [".git", "vendor", "scripts", "docs", "deployments", "pkg"]
excludeFiles = ["structured-folders-files-and-contents.txt"]  # Add the filename to exclude
output_file = "structured-folders-files-and-contents.txt"
```
