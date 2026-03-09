import shutil
import os

#3

folder = "project"

for item in os.listdir(folder):
    full_path = os.path.join(folder, item)

    if os.path.isfile(full_path) and item.endswith(".txt"):
        print(item)

#4
"""
shutil.move("project/file1.txt", "project/data/file1.txt")
print("File moved successfully")
"""


shutil.copy("project/file1.txt", "project/data/file1.txt")
print("File copied successfully")
