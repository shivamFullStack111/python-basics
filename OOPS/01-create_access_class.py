class Student:
    name = ''
    email=''
    course='BCA'
    
    def setNameAndEmail(self,name,email):
        self.name = name 
        self.email = email 
    
    def printData (self):
        print(self.name,self.email,self.course)
    
    
student1  = Student()
student1.college = "LKCTC"         # Instance-specific attribute (exists only for this object) - Dynamic attribute


student1.setNameAndEmail("Shivam","shvam12340987@gmail.com")
student1.printData()