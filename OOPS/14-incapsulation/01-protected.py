# Single underscore is use to define protected attribute and methods 
# Protected method can access and change from own class, child and outside the class 

class Employee:
    _salary = 0
    
    def _showSalary(self):
        print(self._salary)
        
class Person(Employee):
    def changeSalary(self,newSalary):
        self._salary = newSalary
        
obj = Person()

obj.changeSalary(3000)
obj._showSalary()
obj._salary=5000
obj._showSalary()
        
        