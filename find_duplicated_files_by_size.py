import os
from collections import defaultdict


def find_duplicate_files_by_size(directorys):
    # Dictionary to store file sizes and their corresponding file paths
    size_dict = defaultdict(list)
    # Define the minimum file size in bytes (10MB)
    min_size = 50 * 1024 * 1024  # 50 megabytes in bytes

    # Walk through the directory
    for directory in directorys:
        for dirpath, _, filenames in os.walk(directory):
            for filename in filenames:
                # Get the full path of the file
                file_path = os.path.join(dirpath, filename)
                # Get the size of the file
                try:
                    file_size = os.path.getsize(file_path)
                    # Only consider files larger than the defined minimum size
                    if file_size >= min_size:
                        # Append the file path to the list of files with the same size
                        size_dict[file_size].append(file_path)
                except OSError as e:
                    print(f"Error retrieving size for {file_path}: {e}")

    # Filter out file sizes with only one file (no duplicates)
    duplicate_files = {size: paths for size, paths in size_dict.items() if len(paths) > 1}

    return duplicate_files


# Example usage
if __name__ == "__main__":
    directory_paths = ["/Volumes/娱乐", "/Volumes/SANDISK"]
    duplicates = find_duplicate_files_by_size(directory_paths)

    if duplicates:
        print("Potential duplicate files based on size (ignoring files smaller than 50MB):")
        for size, files in duplicates.items():
            print(f"Size: {size} bytes")
            for file in files:
                print(f" - {file}")
    else:
        print("No duplicate files found based on size.")
