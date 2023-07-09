user_size=int(input("eneter the size of list :"))
print(user_size)
list1=[]
print("enter the values of array")
for x in range(user_size):
    user_value=int(input())
    list1.append(user_value)
print("list1 before sorting :",list1)
list1.sort(reverse=True)
print("list1 after sorting",list1)

