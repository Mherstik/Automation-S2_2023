'''
Description: a Python script that backs up specified files or directories 
to a designated backup location.

TODO: 
1) Fix the file. DONE!
2) Make the file ask a location to store the backup 
    and check if the folder exists before using it
3) Then see if we can make it zip a file/folder
'''

import shutil  # what is this? Do you have it?
import os
import zipfile   # add zip capability
import datetime

current = datetime.datetime.now()
#print(current)
current = str(current.year) + str(current.month) + str(current.day) + str(current.hour) + str(current.minute)

def backup_files(source_dir, backup_dir):
    global backup_file
    try:
        # changed from shutil to zipping
        #shutil.copytree(source_dir, backup_dir) # what is copytree?
        
        with zipfile.ZipFile(backup_file, 'w') as archive:
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    archive.write(os.path.join(root,file))
        print("Backup successful!")
    except shutil.Error as e:
        print(f"Error: {e}")

source_directory =  input("Enter the source directory to backup: ")   # '/home/marcus/Documents/GitHub/'
# source_directory = "C:\Users\user\Documents\Automation"
#while True:
backup_directory = input("Enter the destination directory to put the backup: ")# '/home/marcus/Documents/Backup2'
if os.path.exists(str(backup_directory)):
    print(f"Path exists. Appending {current}")
    # change from directory to file for zip
    # backup_directory = str(backup_directory + "_" + current)
    backup_file = str(backup_directory + "_" + current + ".zip")
        #continue
backup_files(source_directory, backup_directory)
