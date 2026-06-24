class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def bark(self):
        print("Bark")

obj = Dog()
obj.sound()             # Inherit method

obj.bark()              # Own method