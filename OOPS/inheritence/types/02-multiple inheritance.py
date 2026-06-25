# Multiple inheritance where Multiple parent class and single child class 


class A:
    def greet(self):
        print("Hello from class A")
        
class B:
    def greet(self):
        print("Hello from class B") 
        
# Python Follows MRO - When object of c call method greet it will find method in this flow  [C → A → B → object] so we have same method in both parent class object whill call mehtod of class A because we have passed A first like " class C(A,B): "
class C(A,B):
    pass


obj = C()


obj.greet()





# MRO stand for Method Resolution Order