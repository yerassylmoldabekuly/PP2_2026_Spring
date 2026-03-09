import shutil
import os

original_file = "input.txt"
copy_file = "input_copy.txt"
backup_file = "backup_input.txt"

if os.path.exists(original_file):
    shutil.copy(original_file, copy_file)
    print("Copied to:", copy_file)

    shutil.copy(original_file, backup_file)
    print("Backup created as:", backup_file)

    os.remove(original_file)
    print("Original file deleted")
else:
    print("Original file does not exist")

