#Import shutil module
import os
import shutil
#Import path module from os
from os import path
#Path to working libffmpeg.so
source_path_fix = "/home/calixte/Downloads/Opera-Assets/libffmpeg.so"
file = os.path.expanduser("~/Downloads/Opera-Assets/libffmpeg.so")
#Path to original libffmpeg.so in Opera
source_path_original = "/usr/lib/x86_64-linux-gnu/opera/libffmpeg.so"
#Path to backup and rename the original libffmpeg.so in Opera
destination_path_backup = "/usr/lib/x86_64-linux-gnu/opera/libffmpeg.so.bak"
#Path to Opera Folder
destination_path = "/usr/lib/x86_64-linux-gnu/opera"

#Checks if the source path is available
if os.path.exists(file):
    #Backup Original file to the same location
    backup_original = shutil.move(source_path_original, destination_path_backup)
    #Copy fix to Opera
    shutil.copy(file, destination_path)
    #Print the message if operation successful
    print(f"Opera Video Playback has been fixed. Moved fix to location: {destination_path}")
else:
    #Print the message if the file does not exist
    print("Could not locate '~/Downloads/Opera-Assets/libffmpeg.so'. Operation Terminated.")