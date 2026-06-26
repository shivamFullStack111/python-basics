def myDecorator(func):
    def wrapper(*args, **kwargs):
        print("This run before student function...")
        func(*args, **kwargs)
        print("This run after student function...")

    return wrapper


@myDecorator
def student(name, age):
    print(f"My Name is {name} and My Age is {age}")


student(name="Shivam", age=21)











"""
==============================
Decorator with **kwargs
==============================

1. **kwargs keyword arguments ko dictionary
   ke form me receive karta hai.

2. wrapper() ke andar func(*args, **kwargs)
   call karte hain taaki original function ko
   saare arguments mil jaye.

@myDecorator ka matlab:
student = myDecorator(student)

Flow:
student(name="Shivam", age=21)
            ↓
wrapper(name="Shivam", age=21)
            ↓
Before Code
            ↓
func(**kwargs)
            ↓
Student Function
            ↓
After Code

Use:
Jab function keyword arguments leta hai,
tab **kwargs use kiya jata hai.
"""