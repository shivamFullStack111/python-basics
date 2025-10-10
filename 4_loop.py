n = int(input("Enter a number to print sum of n numbers: "))


#  print number to n using for loop 

def printNumberUsingForLoop(num):
    for number in range(1,num+1):
       print(number)

def print_n_numbers(num):
    temp=1
    while(temp!=num+1):
      print(temp)
      temp=temp+1
    return

def sumOf_N_Numbers(num):
    sum = 0
    temp = 1
    while(temp!=num+1):
       sum+=temp
       temp+=1
    return sum

print_n_numbers(n)
print(sumOf_N_Numbers(n))
printNumberUsingForLoop(n)


