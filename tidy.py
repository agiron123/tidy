import os
import shutil

print("Running tidy")
#definitions for the paths of the directories that will be used
src = "/home/andre/Desktop"
stuffDir = "/home/andre/Desktop/Stuff"
docsDir = "/home/andre/Desktop/Stuff/Documents"
codeDir = "/home/andre/Desktop/Stuff/Code"
picsDir = "/home/andre/Desktop/Stuff/Pictures"
musicDir = "/home/andre/Desktop/Stuff/Music"
vidsDir = "/home/andre/Desktop/Stuff/Videos"

#create the directory structure if it does not exist already
if not os.path.exists(stuffDir):
    os.makedirs(stuffDir)
if not os.path.exists(docsDir):
    os.makedirs(docsDir)
if not os.path.exists(codeDir):
    os.makedirs(codeDir)
if not os.path.exists(picsDir):
    os.makedirs(picsDir)
if not os.path.exists(vidsDir):
    os.makedirs(vidsDir)
if not os.path.exists(musicDir):
    os.makedirs(musicDir)

extension = "" #extension string, initialize to empty string
src_files = os.listdir(src)
filesMoved = 0
for file_name in src_files:
	full_file_name = os.path.join(src, file_name)
	if (os.path.isfile(full_file_name)):
		extension = file_name[file_name.find("."):]
	
		if(extension == ".txt" or extension == ".docx" or extension == ".odt"):
			dest = docsDir
		elif(extension == ".java" or extension == ".c" or extension == ".h" or extension == ".py"):
			dest = codeDir
		elif(extension == ".jpg" or extension == ".png" or extension == ".raw"):
			dest = picsDir
		#print ("Extension: " + extension)
		#print("Moving " + file_name)
		shutil.move(full_file_name, dest)
		filesMoved = filesMoved + 1
print("File operations are now complete")
print(filesMoved), 
print(" Files Moved")
