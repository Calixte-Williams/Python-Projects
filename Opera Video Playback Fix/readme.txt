Opera Video Playback Fix

ONGOING PROJECT
Seeks to temporarily fix the current problem with Opera-Stable in regards to video playback.
This script makes a backup of the current "libffmpeg.so" in the Opera to "libffmpeg.so.bak".
It then copies the working "libffmpeg.so"  from the Opera-Assets folder.

Requirements:
 - Run with 'sudo'
 - /Opera-Assets folder needs to be located in the /Downloads folder of the User folder.
 - Replace "calixte" with your username in "source_path_fix = "/home/calixte/Downloads/Opera-Assets/libffmpeg.so""


Upcoming Developments:
 - Currently, does not find User Folder using "~", thus only works if the user is defined in Script
 
Feel free to join the effort and offer suggestions.