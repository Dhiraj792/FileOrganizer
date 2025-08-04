import os
import shutil
from datetime import datetime

# Folder where your unsorted files are
source_folder = "C:\\Users\\USER\\Documents"

# Create "arrange" folder inside the project
arrange_folder = os.path.join(os.path.dirname(__file__), "arrange")
os.makedirs(arrange_folder, exist_ok=True)

# File types to organize
file_types = {
    "Pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Code": [".py", ".cpp", ".c", ".java", ".html", ".js"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav", ".aac"]
}

def organize_files():
    print(f"🔄 Organizing files from {source_folder}...\n")
    
    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)

        if os.path.isdir(file_path):
            continue  # Skip folders

        file_ext = os.path.splitext(file_name)[1].lower()
        moved = False

        for folder_name, extensions in file_types.items():
            if file_ext in extensions:
                target_folder = os.path.join(arrange_folder, folder_name)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, file_name))
                moved = True
                print(f"✅ Moved {file_name} to {folder_name}/")
                break

        if not moved:
            other_folder = os.path.join(arrange_folder, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, file_name))
            print(f"📦 Moved {file_name} to Others/")

    print("\n🎉 All files have been organized inside 'arrange' folder.")

if __name__ == "__main__":
    organize_files()
