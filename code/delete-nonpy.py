import glob
import os

# directory path
dir_path = os.getcwd()

# list of files to exclude from deletion
exclude_files = ["README.md"]

# get list of files in the directory
file_list = glob.glob(os.path.join(dir_path, "*"))

# iterate over the list of files
for file_path in file_list:
    # check if the file is not a Python file and is not in the exclude list
    if (
        os.path.isfile(file_path)
        and os.path.splitext(file_path)[1] not in (".py", ".pyw")
        and file_path not in exclude_files
    ):
        os.remove(file_path)
    else:
        pass
