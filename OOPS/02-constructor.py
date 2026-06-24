# Python does not contain "Contructor overloading" like java and c++ 
# we cannot create multiple constructor if we create more then 1 constructor then last constructor overwrites other

class Student:
    name = ''
    email=''
    course="BCA"
    
    def __init__(self):
        print("Default Constructor Run") 
   
        
student1 = Student()
student2 = Student("Shivam","shvam12340987@gmail.com")