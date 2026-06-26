from abc import ABC, abstractmethod

class Rules(ABC):
    @abstractmethod
    def greet(self):
        pass 
    
    
    
class India(Rules):
    
    def greet(self):                        # if we cannot create this mehtod and create object of this class then interpreter will throw error  (TypeError: Can't instantiate abstract class India without an implementation for abstract method 'greet')
        print('Hello India!') 
        

obj = India()
obj.greet()




# Abstraction means define a absteaction method or attribute in a class 
# and the other child class who will inherit abstract class also have to
# define the same method and attributes that defined in abstraction class