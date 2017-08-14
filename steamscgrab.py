#! python3.5
import os, shutil

os.chdir("C:\\Program Files (x86)\\Steam\\userdata")
distt = "C:\\Program Files (x86)\\Steam\\_found" # Where you want the pictures
if not os.path.exists(distt):
    os.mkdir(distt)
path = os.getcwd()
print(path)
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith((".jpg", ".png", ".jpeg")):
            folder = root.split("\\")[-1] ######## Folder name where pictures are found
            fdist = distt+"\\"+folder     ######## "C:\\Program Files (x86)\\Steam\\_found" + folder
            print(file)
            if not os.path.exists(fdist):
                os.mkdir(fdist)
            shutil.copy(root+"\\"+file, fdist)
print("Done!")
