

def myDecorator(func):
    def wrapper():
        print("This run before greeting...")
        func()
        print("This run after greeting...")
    
    return wrapper

@myDecorator
def greeting():
    print("Hello...")
    
greeting()
    
    
    
    
    
    
    
    
    
""""
1. myDecorator() ek function ko input me leta hai.
2. Iske andar wrapper() function create hota hai.
3. wrapper() me extra code likhte hain jo original function ke
   before aur after execute hoga.
4. wrapper ko return kar dete hain.

@myDecorator ka matlab:
greeting = myDecorator(greeting)

Ab jab greeting() call hota hai to actual me wrapper() execute hota hai.

Flow:
greeting()
   ↓
wrapper()
   ↓
Before Code
   ↓
Original Function (func())
   ↓
After Code

Decorator ka use bina original function ko modify kiye
usme extra functionality add karne ke liye kiya jata hai.
"""