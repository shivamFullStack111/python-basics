class A:
    def greet(self):
        print("Hello")
        
class B(A):
    pass 

obj = B()
obj.greet()