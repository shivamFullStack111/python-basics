# __str__ method call when print the object 

class Student:
    def __str__(self):
        return "Student Object"

s = Student()

print(s)