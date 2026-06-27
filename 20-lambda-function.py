#  Lambda Function is anonymous (naam ke bina) function, which use for small task in single line. 

# SYNTAX: 
# lambda arguments: expression 


addition = lambda a,b: a+b 

check = lambda a: "even" if a%2==0 else "odd"

print(addition(5,6))
print(check(5))