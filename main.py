#Import Folders
import os
import shutil

# Step 1: Get the Desktop path
desktop_path = os.path.join(os.path.expanduser("~"), "Documents")

#  Step 2: Add a dictionary that maps folder names to file extensions
folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Music": [".mp3", ".wav", ".aac"],
    "Others": []  # Files that don’t match any category
}

# Step 3: Create folders if they don't exist
for folder_name in folders.keys():
    folder_path = os.path.join(desktop_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Step 4: Move files into appropriate folders
for file_name in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, file_name)
    
    # Skip folders
    if not os.path.isfile(file_path):
        continue
    
    # Check file extension and move
    moved = False
    for folder_name, extensions in folders.items():
        if any(file_name.endswith(ext) for ext in extensions):
            shutil.move(file_path, os.path.join(desktop_path, folder_name, file_name))
            moved = True
            break
    
    # Move files that don't match any category to 'Others'
    if not moved:
        shutil.move(file_path, os.path.join(desktop_path, "Others", file_name))

# Step 5: Print success message
print("Desktop organized successfully!")
