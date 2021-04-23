import os
import shutil
import time


def main():
    path = "/Users/Jacob/Whitehatprojects/FileForDeletion"
    days = 1

    ExpiryDate = time.time() - (days * 24 * 60 * 60)
    print(ExpiryDate / 24 * 60 * 60)

    if os.path.exists(path):
        # print("True!")
        for rootFolders, folders, files in os.walk(path):
            # print(str(rootFolders) + " " + "Root Folder")
            print(str(folders) + " " + "Folders")
            # print(str(files) + " " + " Files")

            if ExpiryDate >= os.stat(rootFolders).st_ctime:
                shutil.rmtree(rootFolders)
            else:
                for folder in folders:
                    folderPath = os.path.join(rootFolders, folder)
                    print(folderPath)
                    if ExpiryDate >= os.stat(folderPath).st_ctime:
                        shutil.rmtree(folderPath)
                for filing in files:
                    filePath = os.path.join(rootFolders, filing)
                    if ExpiryDate >= os.stat(filePath).st_ctime:
                        os.remove(filePath)


main()
