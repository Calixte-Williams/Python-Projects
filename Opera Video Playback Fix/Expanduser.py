# Python program to explain os.path.expanduser() method

# importing os.path module

import os.path
from typing import IO

# Path
path = "~/Downloads/Opera-Assets/libffmpeg.so"

# Expand an initial ~ component
# in the given path
# using os.path.expanduser() method
full_path = os.path.expanduser(path)

# print the path after
# expanding the initial ~ component
# in the given path
print(full_path)

fix = full_path
print(str(fix))
os.path.exists(fix)
