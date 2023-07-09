list_size=int(input("enter the size of arrays :"))
print(list_size)
parent=[]

for y in range(list_size):
    print(f"enter {list_size} values for list1 : ")
    list1=[]
    for x in range(list_size,):
        user_value = int(input())
        list1.append(user_value)
        list1
    parent.append(list1)
    print(parent)
parent2=[]

for y in range(list_size):
    print(f"enter {list_size} values for list2 : ")
    list2=[]
    for x in range(list_size,):
        user_value = int(input())
        list2.append(user_value)
        # list2
    parent2.append(list2)
    print(parent2)

list3=[]
for x in range(list_size):
    sublist3=[]
    for y in range(list_size):
        sum=parent[x][y]+parent2[x][y]
        sublist3.append(sum)
    list3.append(sublist3)
print("sum  of 2 list:")
for sublist in list3:
    print(sublist)








# first_element = parant[0][2] + parent2[0]2]
# print(first_element)

# list1 = [[1,2,3], [432], [424]]

