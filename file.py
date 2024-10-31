import os

#one specifice file rename
if os.path.exists("input.txt"):
    os.rename("input.txt", "fileText.js")
    print("File renamed successfully.")
else:
    print("File not found!")



#coping the file
import shutil

if os.path.exists("source.txt"):
    shutil.copy("source.txt", "destination.txt")
    print("File copied successfully.")
else:
    print("Source file not found!")

