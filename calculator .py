print("select any one operation:")
print("1.Addition:")
#k=x+y
print("k=x+y")
print("2.Subtraction:")
#k=x-y
print("k=x-y")
print("3.Multiplication:")
#k=x*y
print("k=x*y")
print("4.Divison:")
#k=x/y
print("k=x/y")
while True:
    n=input("enter (1/2/3/4):")
    n=int(n)
    if n>0 and n<5:
        x=input("enter first number:")
        y=input("enter second number:")
        x=float(x)
        y=float(y)
        if n==1:
           k=x+y
           print("The value of addition:")
           print(k)
        elif n==2:
           k=x-y
           print("The value of subtraction:")
           print(k)
        elif n==3:
           k=x*y
           print("The value of multiplication:")
           print(k)
        else:
           k=x/y
           print("The value of division:")
           print(k)
         
    
    else:
        print("invalid input")    
    p=input("Next calculation (yes/no):")
    if p=="no":
        break
        