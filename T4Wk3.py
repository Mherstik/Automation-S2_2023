'''
Description: a
Python script that backs up specified files or directories 
to a designated backup location.

TODO: 
1) Fix the file.
2) Then see if we can make it zip a file/folder
'''

import shutil  # what is this? Do you have it?
import os

def backup_files(source_dir, backup_dir):
    try:
        shutil.copytree(source_dir, backup_dir) # what is copytree?
        print("Backup successful!")
    except shutil.Error as e:
        print(f"Error: {e}")

source_directory = '/home/marcus/Documents/GitHub/'
# source_directory = "C:\Users\user\Documents\Automation"
backup_directory = '/home/marcus/Documents/Backup2'
backup_files(source_directory, backup_directory)
