class Animal:
    legs = 4
    
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def bark(self):
        print("Bark")

obj = Dog()
obj.sound()             # Inherited method
print(obj.legs)         # Inherited attribute

obj.bark()              # Own method
