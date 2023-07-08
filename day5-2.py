size = int(input("Enter the size of the list: "))
list1= []
print("Enter the values of the array:")
for x in range(size):
    value = int(input())
    list1.append(value)


count=0
for num in list1:
    if num % 2 == 0:
        count=count+1
print("Number of even numbers in the given array is",count)

