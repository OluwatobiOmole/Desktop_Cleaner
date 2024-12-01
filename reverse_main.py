# Import relevant libraries 
import os
import shutil

# Step 1: Get the Desktop path
desktop_path = os.path.join(os.path.expanduser("~"), "Documents")

# Step 2: Define folder names (same as in the original script)
folder_names = ["Images", "Videos", "Documents", "Music", "Others"]

# Step 3: Loop through each folder and move files back to the desktop
for folder_name in folder_names:
    folder_path = os.path.join(desktop_path, folder_name)
    
    # Check if the folder exists
    if os.path.exists(folder_path):
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            
            # Move each file back to the desktop
            shutil.move(file_path, os.path.join(desktop_path, file_name))
        
        # Optional: Remove the now-empty folder
        os.rmdir(folder_path)

print("Files have been restored to the desktop!")