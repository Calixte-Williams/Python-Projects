#Import shutil module
import shutil
#Import path module from os
from os import path
#Path to working libffmpeg.so
source_path_fix = "/home/calixte/Downloads/0.52.2-linux-x64/libffmpeg.so"
source_path_original = "/usr/lib/x86_64-linux-gnu/opera/libffmpeg.so"
#Checks if the source path is available
if path.exists(source_path_fix):
    destiniation_path_backup = "/usr/lib/x86_64-linux-gnu/opera/libffmpeg.so.bak"
    destiniation_path = "/usr/lib/x86_64-linux-gnu/opera"
    #Backup Original file to the same location
    backup_original = shutil.move(source_path_original, destiniation_path_backup)
    #Copy fix to Opera
    fix = shutil.copy(source_path_fix, destiniation_path)
    #Print the message if operation successful
    print(f"Opera Video Playback has been fixed. Moved fix to location: {destiniation_path}")
else:
    #Print the message if the file does not exist
    print("Could not locate file. Operation Terminated.")