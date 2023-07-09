def get_list():
    user_size=int(input("enter the size for list1 :"))
    list1=[]
    print(f" enter {user_size} values for list1")
    for x in range(user_size):
        user_values=int(input())
        list1.append(user_values)
    # print(list1)
    return list1
    
list_from_getlist = get_list()
# print(list_from_getlist)

def diplayArray(x):
    print("display the list value inside the display list function",x)


diplayArray(list_from_getlist)
        

    