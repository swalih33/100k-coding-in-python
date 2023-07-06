    
mark=float(input("enter your total mark percentage:"))
print("your mark percentage is",mark)
if(mark>100):
    print("you entered exceed limit ! please enter limit of 100")
elif(mark>90 and mark<100):
    print("grade=A")
elif(mark>=80 and mark<=89):
    print("grade=B")
elif(mark>=70 and mark<=79):
    print("grade=C")
elif(mark>=60 and mark<=69):
    print("grade=D")
elif(mark>=50 and mark<=59):
    print("grade=E")
else:
    print("failed")
    
    