



class Animal:
    
    def __init__(self,name):
        self.name = name
        
    def dataPrint(self):
        print(self.name,self.height)



class Dog(Animal):
    
    def __init__(self, name,height):
        super().__init__(name)                   # super target the parent class 
        self.height = height

obj = Dog("Tommy",1.8)
obj.dataPrint()
















