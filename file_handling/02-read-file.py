# If you are using with as then it will automatically close the file 
# if you are using direct open function without with as then you have to close the file 

try:
    with open("dummy.txt",'r') as fs:
        print(fs.read())
        
except Exception as err:
    print(f"Error: {err}")