import os
import shutil
import datetime

def categorize_by_size(file_size):
    # Define size categories and their ranges in bytes
    size_categories = {
        'small': (0, 1024),        # Up to 1 KB
        'medium': (1025, 1024 * 1024),  # 1 KB to 1 MB
        'large': (1024 * 1025, float('inf'))  # Larger than 1 MB
    }

    for category, (min_size, max_size) in size_categories.items():
        if min_size <= file_size < max_size:
            return category

    return 'unknown'

def organize_files(source_dir, destination_dir, organize_by_type=True, organize_by_date=True, organize_by_size=True):
    # Create a dictionary to map file extensions to corresponding folders
    file_types = {
        'images': ['.png', '.jpg', '.jpeg', '.gif'],
        'documents': ['.pdf', '.docx', '.txt'],
        'videos': ['.mp4', '.avi', '.mkv'],
        'other': []  # Add more categories and file extensions as needed
    }

    # Create destination subdirectories if they don't exist
    if organize_by_type:
        for folder in file_types:
            folder_path = os.path.join(destination_dir, folder)
            os.makedirs(folder_path, exist_ok=True)

    if organize_by_date:
        for year in range(2010, 2030):  # Adjust the range based on your needs
            year_folder = os.path.join(destination_dir, str(year))
            os.makedirs(year_folder, exist_ok=True)

            for month in range(1, 13):
                month_folder = os.path.join(year_folder, f"{month:02d}")
                os.makedirs(month_folder, exist_ok=True)

    if organize_by_size:
        for size_category in ['small', 'medium', 'large']:
            size_folder = os.path.join(destination_dir, size_category)
            os.makedirs(size_folder, exist_ok=True)

    # Scan the source directory and organize files
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        if os.path.isfile(file_path):
            # Determine the file type based on extension
            file_type = None
            for category, extensions in file_types.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    file_type = category
                    break

            if organize_by_type and file_type:
                # Move the file to the corresponding subdirectory
                destination_folder = os.path.join(destination_dir, file_type)
                destination_path = os.path.join(destination_folder, filename)
                shutil.move(file_path, destination_path)
                print(f"Moved: {filename} to {file_type} folder")

            if organize_by_date:
                # Get the creation date of the file
                creation_time = os.path.getctime(file_path)
                creation_date = datetime.datetime.fromtimestamp(creation_time)

                # Determine the destination folder based on creation date
                destination_folder = os.path.join(
                    destination_dir,
                    str(creation_date.year),
                    f"{creation_date.month:02d}",
                )

                # Move the file to the corresponding subdirectory
                destination_path = os.path.join(destination_folder, filename)
                shutil.move(file_path, destination_path)
                print(f"Moved: {filename} to {creation_date.year}/{creation_date.month:02d} folder")

            if organize_by_size:
                # Get the size of the file in bytes
                file_size = os.path.getsize(file_path)

                # Determine the destination folder based on file size
                size_category = categorize_by_size(file_size)
                destination_folder = os.path.join(destination_dir, size_category)
                destination_path = os.path.join(destination_folder, filename)
                shutil.move(file_path, destination_path)
                print(f"Moved: {filename} to {size_category} folder")

# Get source and destination directories from the user
source_directory = input("Enter the source directory path: ")
destination_directory = input("Enter the destination directory path: ")

# Ask the user how they want to organize the files
organize_by_type = input("Organize by file type? (yes/no): ").lower() == 'yes'
organize_by_date = input("Organize by creation date? (yes/no): ").lower() == 'yes'
organize_by_size = input("Organize by size? (yes/no): ").lower() == 'yes'

organize_files(source_directory, destination_directory, organize_by_type, organize_by_date, organize_by_size)
