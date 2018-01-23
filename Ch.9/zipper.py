#! /usr/bin/env python3
'''
zipper.py - Copies an entire folder and its contents into a .zip file,
the name of which increments with each backup, e.g. "zipped_1" > "zipped_2"

for foldername, subfolders, filenames in os.walk(folder):
        |           |           |                   |
        Current directory in the loop, os.walk() does not change the
        working directory.      |                   |
                    |           |                   |
                    Every folder inside "foldername"|
                                |                   |
                                Every file inside "foldername" 
                                                    |
                                                    os.walk takes an absolute
                                                    path argument
'''

import zipfile, os

def backupToZip(folder):
    
    # Backup the entire contents of "folder" into a ZIP file:
    
    total_zipped = 0
    folder = os.path.abspath(folder)
    
    # Decide filename based on existing files:
    
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number += 1
        
    # Create the ZIP file:
    print('Creating {}...'.format(zipFileName))
    
    backupZIP = zipfile.ZipFile(zipFileName, 'w')
    
    # Walk the entire folder tree and compress the files in each folder:
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in {}...'.format(foldername))
        
        # Add current folder to the ZIP file:
        backupZIP.write(foldername)
        
        # Add all the files in this folder to the ZIP file:
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # Don't backup the backups
            
            total_zipped += 1
            backupZIP.write(os.path.join(foldername, filename))
            
    print('{} items zipped.'.format(total_zipped))
    
folder = input('Please provide the absolute path of the folder which\'s contents you want to ZIP: ')
backupToZip(folder)
