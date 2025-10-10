tup = tuple()

num = int(input("Enter number of element in tuple: "))

for i in range(1,num+1):
    tup=tup+(int(input(f"Enter {i} value: ")),)

print("Tuple: ",tup)

findNumber=int(input("Enter number to find it is exist in tuple: "))

if findNumber in tup:
    print("Exist")
else:
    print("Not Exist")