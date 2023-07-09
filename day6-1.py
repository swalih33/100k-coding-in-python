att=int(input("enter the attempt in number:"))
for x in range(att):
    string=input("enter a string :")
    reversed_string=string[::-1]
    print("entered string :",string)
    print("reversed string :",reversed_string)
    if(string==reversed_string):
        print("entred string is a palindrome")
    else:
        print("entered string is not palindrome")