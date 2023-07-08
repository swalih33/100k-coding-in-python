list_size=int(input("enter the size of arrays :"))
print(list_size)
list1 = []
print(list1)
print(f"enter {list_size} values for list1 : ")
for x in range(list_size):
    user_value = int(input())
    list1.append(user_value)
    # print("list1", list1)
# list2_size=int(input("enter the values of arrray 2 :"))
list2 = []
# print(list2)
print(f"enter {list_size} value for list2 : ")
for y in range(list_size):
    list2_value= int(input())
    list2.append(list2_value)
    # print("list2",list2)
    
print("list1 before swapping: ", list1)
print("list2 before swapping: ", list2)
temp=list2
list2=list1
list1=temp

print("list1 after swapping ",list1)
print("list2 after swapping ",list2)