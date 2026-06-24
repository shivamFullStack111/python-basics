class Student:
    name = ''
    email=''
    course='BCA'
    
    # Class method - works with the class itself, not a specific object.
    
    @classmethod
    def printCourse(cls):
        print(cls.course)
    
    
Student().printCourse
