from pathlib import Path

name = str(input("Enter file name to create: "))

p = Path(name) 

if(p.exists() and p.is_file()):
    print(f"FILE: ''{p}'' is already exist")

else:
    with open(name,'w') as fa:
        print("File created")