# Double underscore is use to define private attribute and methods 
# Private method can access and change from only its own class

class Employee:
    __salary = 0
    
    def __init__(self,newSalary):
        self.__previousSalary = self.__salary                 # Dynamic Private attribute 
        self.__salary=newSalary
    
    def _showSalary(self):
        print(self.__salary)


obj = Employee(444)

obj._showSalary()
        
        