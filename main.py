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

