from pathlib import Path


oldName = "dummy.txt"
newName = "dummy2.txt"

p = Path(oldName)

try:
    p.rename(newName)

except Exception as err:
    print(err)
