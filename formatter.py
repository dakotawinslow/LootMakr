import json
import os
import shutil
import unidecode

# clear the data/ folder
shutil.rmtree("data/")
os.mkdir("data/")

# make a list of the files in old-data/
files = os.listdir("old-data/")

# loop through the files
for filename in files:
    # print(f"Processing {filename}...")
    # change unicode to ascii
    with open(f"old-data/{filename}", "r", encoding="utf-8") as file:
        data = file.read()
    data = unidecode.unidecode(data)
    with open(f"old-data/{filename}", "w") as file:
        file.write(data)

    # open file and read it
    with open(f"old-data/{filename}", "r") as file:
        data = file.readlines()

    try:
        # Remove all charcters in the first line before the '['
        data[0] = "[" + data[0].split("[")[1]
        # Remove all characters in the last line after the ']'
        data[-1] = data[-1].split("]")[0] + "]"
    except IndexError:
        # Remove all charcters in the first line before the '{'
        data[0] = "{" + data[0].split("{")[1]
        # Remove all characters in the last line after the '}'
        data[-1] = data[-1].split("}")[0] + "}"

    # make the new filename
    filename = filename.split(".")[0]
    filename = filename + ".json"

    # write the file to the data/ folder
    with open(f"data/{filename}", "w") as file:
        file.write("".join(data))

    # confirm that the new file is proper JSON
    try:
        with open(f"data/{filename}", "r") as file:
            json.load(file)
        print(f"{filename}: File written successfully")
    except json.JSONDecodeError:
        print(f"{filename}: File is not valid JSON")
