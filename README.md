# FileOrganizer
# 🗂️ File Organizer with Auto-Sorting into "arrange" Folder

This Python project organizes your files from a selected folder (like `Downloads` or `Documents`) into specific categories — such as Pictures, Documents, Spreadsheets, Code, etc. All organized files are moved into a single folder called `arrange`.

---

## 📌 Features

- Automatically sorts files based on their extensions
- Moves files into subfolders like:
  - `Pictures/`
  - `Documents/`
  - `Spreadsheets/`
  - `Code/`
  - `Videos/`
  - `Music/`
  - `Others/` (for unrecognised file types)
- Creates a clean `arrange/` directory to store everything
- Easy to set up and modify

---

## 🛠️ How It Works

1. Set the path of the folder you want to organize in the `source_folder` variable.
2. Run the script.
3. All files from the source folder will be moved into the `arrange/` folder, organized by category.

---

## 📁 Folder Structure
FileOrganizer/
├── organize.py
├── arrange/
│ ├── Pictures/
│ ├── Documents/
│ ├── Spreadsheets/
│ ├── Code/
│ ├── Music/
│ ├── Videos/
│ └── Others/


