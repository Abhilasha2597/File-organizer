import os #  Used to work with files and folders (create folder, list files, paths
import shutil # Used to move files from one folder to another

# Define Folder Path
path = r"C:\Users\abhil\Downloads"

# Define file categories Key → Folder name
# Value → File extensions that go into that folder
folders = {
    "Images": [".jpg", ".png"],
    "PDF": [".pdf"],
    "Excel": [".xlsx",".csv"],
    "Text": [".txt"],
    "Word": [".docx",".doc"],
    "zip":[".zip"],
    "ppt":[".pptx"],
    "powerBI":[".pbix"],
    "tableau":[".exe"]

}

# Create folders automatically
for folder in folders: #Loop through dictionary keys
    folder_path = os.path.join(path, folder) #safely joins paths. create full folder path
    if not os.path.exists(folder_path): #Check if folder already exists If not → create the folder
        os.mkdir(folder_path)

# Read all files
files = os.listdir(path) # List the directories access to files and folders

# Move files
for file in files:
    file_path = os.path.join(path, file)  #safely joins paths . create full folder path 

    if os.path.isfile(file_path):#Checks if it is a file (not a folder)
        for folder, extension in folders.items(): 
            for ext in extension:
                if file.endswith(ext):
                    shutil.move(file_path, os.path.join(path, folder, file)) #Moves file to correct folder.
                    print(file, "moved to", folder) 