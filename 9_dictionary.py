student = {
    "name":"shivam",
    "class":"BCA",
    "rollNo":2332363
}

print(student.keys()) #get all keys 
print(student.values()) #get all values 
print(student.items()) #get all key values

print(student)

# access single value 
print(student["class"])

# remove specific key value 
student.pop("name")
print(student)

# remove last inserted key pair 
student.popitem()
print(student)

# adding new key value 
student["age"] = 21 
print(student)

# checking if the key is exist or not in dictionary 
if "age" in student:
    print("age exist")
else:
   print ("age doesn't exist")