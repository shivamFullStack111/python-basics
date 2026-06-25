class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):   # Overriding
        print("Dog barks")

dog = Dog()
dog.sound()  

# Output -
# Dog barks