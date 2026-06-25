# Parent Class
class Animal:
    def eat(self):
        print("Animal can eat")

# Child Class 1
class Dog(Animal):
    def bark(self):
        print("Dog can bark")

# Child Class 2
class Cat(Animal):
    def meow(self):
        print("Cat can meow")

# Objects
dog = Dog()
cat = Cat()

# Dog methods
dog.eat()      # inherited from Animal
dog.bark()

print()

# Cat methods
cat.eat()      # inherited from Animal
cat.meow()