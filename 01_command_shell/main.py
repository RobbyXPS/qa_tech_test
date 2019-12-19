# TODOs
# 1. Update hard coded replace string 'contour' with regex that will match case sensitivity
# 2. Test with different file types 1.file with many case sensitive versions of 'contour', 2. empty text file, 3. string exist multiple times on same line, 4. large file with old english characters
# 3. Create log output that gives user more info about which files were touched and how many times a match was found

# To Run script:
# Install python3 https://www.python.org/download/releases/3.0/
# In terminal > navigate to correct directory (e.g. `cd development/interview_tests/jama/qa_tech_test/01_command_shell`)
# In finder review files to be updated in 'files_to_update' folder > notice they have strings 'contour' in them and no strings of 'jamaconnect'
# Run the script in the terminal via `python3 main.py` > enter
# In finder review files to be updated in 'files_to_update' folder > notice they no longer have strings 'contour' in them, and they have been updated to string 'jamaconnect'

# import os module to interact with system functionality
import os

# capture the dir where files waiting to be updated need to be moved to before running script
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
