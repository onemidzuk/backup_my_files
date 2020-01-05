import os
import zipfile
import time

source_dir = [i for i in input("Please type the absolute path to directories you want to backup separated by space:\n").split()]

target_dir = input("Please type the absolute path to your backup storage directory:\n")

today_dir = target_dir + os.sep + time.strftime('%Y%m%d')       # Creating the name of storage directory named by current date

now_fname = time.strftime('%H%M%S')                             # Creating the name of backup file named by current time

if not os.path.exists(today_dir):                               # Creating backup storage directory if it is the first backup of today
    os.mkdir(today_dir)                                         # and directory is not exist.
    print('Directory is succesfully created!')


comment = input('Input your comment:')                          # Comment for your backup file

if len(comment) == 0:
    target_arc = today_dir + os.sep + now_fname + '.zip'        # Concatenate comment to file name if it was typed
else:
    target_arc = today_dir + os.sep + now_fname + '_' + \
             comment.replace(' ', '_') + '.zip'                 #  and replace spaces by underscores

archive = zipfile.ZipFile(target_arc, 'w')                      # creating the zipfile

for source_dirs in source_dir:                                # iteration by source dirs
    for root, dirs, files in os.walk(source_dirs):            # walk by dirs and files with os.walk
        for file in files:
            archive.write(os.path.join(root, file))           # creating absolute paths to source files and writing them to the archive

archive.close()

print('Backup is succesfully competed. Your copy is in', today_dir)