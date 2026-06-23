# Apend mode add content it can'nt re-write complete file and creat file 


from pathlib import Path



fileName = "dummy.txt"

textToWrite ="My name is shivam and i'm a gen ai developer"

p = Path(fileName)

try:
    with open(fileName,'w') as fs:
        fs.write(textToWrite)
        print("Content write successfull!")
        
except Exception as err:
    print(f"Error: {err}")