sett = set()
num = int(input("Enter number of elements in set: "))

for i in range(1,num+1):
    n = int(input(f"Enter number {i}: "))
    sett.add(n)

print("Set before remove element ")
print("Set elements are: ",sett)

removeElement = int(input("Enter value to remove: "))

# i use discard function instead of remove 
# because remove return error if the value doesn't exist in set 
sett.discard(removeElement)

print("Set after remove element ")
print("Set elements are: ",sett)
