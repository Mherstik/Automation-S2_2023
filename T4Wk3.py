'''
Description: a Python script that backs up specified files or directories to a designated backup location.
'''

import shutil  # what is this? Do you have it?
import os

def backup_files(source_dir, backup_dir):
    try:
        shutil.copytree(source_dir, backup_dir) # what is copytree?
        print("Backup successful!")
    except shutil.Error as e:
        print(f"Error: {e}")

source_directory = '/path/to/source'
backup_directory = '/path/to/backup'
do_backup(source_dir, backup_dir)
