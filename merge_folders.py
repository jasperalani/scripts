# merge_folders.py
# - The script scans a `source_dir` (default: `peep-unzipped`) for subdirectories whose names start with `append_dir` (default: "Lil Peep Discography Updated").
# - For each matching subdirectory, it looks inside a nested folder (also named "Lil Peep Discography Updated" by default).
# - It recursively walks through all files in these source folders.
# - For every file found, it copies the file to the corresponding location in the `target_dir` (default: "Lil Peep Discography Updated") only if the file does not already exist there.
# - The directory structure is preserved.
# - Progress is printed to the console as files are copied.

import os
import shutil
from pathlib import Path

def merge_folders(source_dir, target_dir, append_dir = "Lil Peep Discography Updated"):
    # Create target directory if it doesn't exist
    target_path = Path(target_dir)
    target_path.mkdir(parents=True, exist_ok=True)
    
    # Get all source directories
    source_dirs = [d for d in os.listdir(source_dir) 
                  if os.path.isdir(os.path.join(source_dir, d)) 
                  and d.startswith("Lil Peep Discography Updated")]
    
    # Process each source directory
    for source_subdir in source_dirs:
        source_path = Path(source_dir) / source_subdir / append_dir
        if not source_path.exists():
            continue
            
        # Walk through the source directory
        for root, dirs, files in os.walk(source_path):
            # Calculate relative path from source
            rel_path = os.path.relpath(root, source_path)
            if rel_path == '.':
                rel_path = ''
            
            # Create corresponding target directory
            target_subdir = target_path / rel_path
            target_subdir.mkdir(parents=True, exist_ok=True)
            
            # Copy files
            for file in files:
                source_file = Path(root) / file
                target_file = target_subdir / file
                
                # Only copy if target doesn't exist
                if not target_file.exists():
                    shutil.copy2(source_file, target_file)
                    print(f"Copied: {source_file} -> {target_file}")

if __name__ == "__main__":
    source_dir = "peep-unzipped"
    target_dir = "Lil Peep Discography Updated"
    merge_folders(source_dir, target_dir)
    print("Folder merging completed!") 