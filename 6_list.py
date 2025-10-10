
nums = []

print("Enter 5 numbers: ")
for i in range(0,5):
    n = int(input())
    nums.append(n)


def printNumbersOfList(list):
    for n in list:
        print(n, end=" ")
    print('\n')

printNumbersOfList(nums)


print("Maximum: ",max(nums))
print("Minimum: ",min(nums))
print("Average: ",sum(nums)/len(nums))