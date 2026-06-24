class Student:
    name = ''
    email=''
    course='BCA'

    # Static method - utility method that belongs to the class but doesn't use self or cls.
    
    @staticmethod
    def add(a,b):
        return a + b
    

obj = Student()

obj.add(4,9)           # Call using object
Student().add(5,9)     # Call using class
    
