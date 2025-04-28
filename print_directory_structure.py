import os
import sys

def write_directory_structure(path, output_file, indent=0):
    """
    Recursively write the directory structure starting from the given path to a file.
    Args:
        path (str): The starting directory path
        output_file (file): The file object to write to
        indent (int): Current indentation level
    """
    # Write the current directory name
    output_file.write('  ' * indent + '📁 ' + os.path.basename(path) + '\n')
    
    try:
        # List all items in the current directory
        items = os.listdir(path)
        
        # Sort items to maintain consistent order
        items.sort()
        
        for item in items:
            item_path = os.path.join(path, item)
            
            # If it's a directory, recursively write its contents
            if os.path.isdir(item_path):
                write_directory_structure(item_path, output_file, indent + 1)
            # If it's a file, write it
            else:
                output_file.write('  ' * (indent + 1) + '📄 ' + item + '\n')
                
    except PermissionError:
        output_file.write('  ' * (indent + 1) + '⚠️ [Permission Denied]\n')
    except Exception as e:
        output_file.write('  ' * (indent + 1) + f'⚠️ [Error: {str(e)}]\n')

def main():
    # Check if a path was provided as an argument
    if len(sys.argv) > 1:
        start_path = sys.argv[1]
    else:
        # Use current directory if no path provided
        start_path = os.getcwd()
    
    # Set default output filename
    output_filename = "directory_structure.txt"
    if len(sys.argv) > 2:
        output_filename = sys.argv[2]
    
    # Check if the path exists
    if not os.path.exists(start_path):
        print(f"Error: The path '{start_path}' does not exist.")
        sys.exit(1)
    
    try:
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(f"Directory Structure for: {start_path}\n\n")
            write_directory_structure(start_path, output_file)
        print(f"Directory structure has been written to '{output_filename}'")
    except Exception as e:
        print(f"Error writing to file: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()