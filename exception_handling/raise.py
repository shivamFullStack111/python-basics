age = -10


try:
    if(age<0 or age>120):
        raise ValueError("Invalid Age")              # raising an error  and handling in expert block
    else:
        print("your age is correct")
    
except Exception as err:
    print(f"Error {err}")