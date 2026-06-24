class Animal:
    legs = 4
    
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def bark(self):
        print("Bark")

obj = Dog()
obj.sound()             # Inherit method
print(obj.legs)         # Inherit attribute

obj.bark()              # Own method
