import os
import shutil

#Note: This currently only works on Mac
#TODO: Check which OS user is on and adjust file path accordingly
print("Running tidy")
#definitions for the paths of the directories that will be used
src = "/Users/andre/Desktop"
stuffDir = src + "/MyStuff"
print "StuffDir Location: " + stuffDir
docsDir = stuffDir + "/Documents"
codeDir = stuffDir + "/Code"
picsDir = stuffDir + "/Pictures"
musicDir = stuffDir + "/Music"
vidsDir = stuffDir + "/Videos"

#create the directory structure if it does not exist already
print "Creating Directory Structure"
if not os.path.exists(stuffDir):
    print "Creating Stuff directory"
    os.makedirs(stuffDir)
if not os.path.exists(docsDir):
    print "Created Documents Directory"
    os.makedirs(docsDir)
if not os.path.exists(codeDir):
    print "Created Code Directory"
    os.makedirs(codeDir)
if not os.path.exists(picsDir):
    print "Created Pictures Directory"
    os.makedirs(picsDir)
if not os.path.exists(vidsDir):
    print "Created Videos Directory"
    os.makedirs(vidsDir)
if not os.path.exists(musicDir):
    print "Created Music Directory"
    os.makedirs(musicDir)


extension = "" #extension string, initialize to empty string
src_files = os.listdir(src)
filesMoved = 0
for file_name in src_files:
  dest = stuffDir
  full_file_name = os.path.join(src, file_name)
  if (os.path.isfile(full_file_name)):
    extension = file_name[file_name.find("."):]
    if(extension == ".txt" or extension == ".docx" or extension == ".odt"):
      dest = docsDir
    elif(extension == ".java" or extension == ".c" or extension == ".h" or extension == ".py"):
      dest = codeDir
    elif(extension == ".jpg" or extension == ".png" or extension == ".raw"):
      dest = picsDir
    shutil.move(full_file_name, dest)
    filesMoved = filesMoved + 1
print("File operations are now complete")
print(filesMoved),
print(" Files Moved")
