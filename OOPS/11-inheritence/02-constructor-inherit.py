

class Animal:
    
    def __init__(self,name):
        self.name = name



class Dog(Animal):
    
    def printName(self):
        print(self.name)

obj = Dog("Tommy")

obj.printName()
