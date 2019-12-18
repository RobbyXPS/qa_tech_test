# import os module to interact with system functionality
import os

# capture the dir where files waiting to be updated need to be moved to before running program
file_dir = os.getcwd() + "/files_to_update"

# iterate through each file in the dir
for subdir, dirs, files in os.walk(file_dir):
    for file in files:
        # capture full file path that will be read/write from
        tempPath = os.path.join(subdir, file)

        # open the file so you can read it's contents, it closes itself after the block ends
        # use python built in .replace method to update strings
        with open(tempPath, "r") as readFile:
            readText = readFile.read().replace("contour", "jamaconnect")

        # open the file so you can write to it, it closes itself after the block ends
        # use python built in .write function to update the new file passing in the updated strings from the first block
        with open(tempPath, "w") as writeFile:
            writeFile.write(readText)
