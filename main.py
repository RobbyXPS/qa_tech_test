import os

# encode the specified filename to the filesystem encoding with ‘surrogateescape‘ error handler
#import os
file_dir = os.getcwd() + "/files_to_update"
# print(cwd)

for subdir, dirs, files in os.walk(file_dir):
    for file in files:
        print(os.path.join(subdir, file))

# open the file so you can read it's contents, it closes itself after the block ends
# use python built in .replace method to update strings
with open("./files_to_update/Lipsum_03.txt", "r") as readFile:
    readText = readFile.read().replace("contour", "jamaconnect")

# open the file so you can write to it, it closes itself after the block ends
# use python built in .write function to update the new file passing in the updated strings from the first block
with open("./files_to_update/Lipsum_03.txt", "w") as writeFile:
    writeFile.write(readText)
