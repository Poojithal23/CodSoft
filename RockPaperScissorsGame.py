import string
import random
while(True):
    #R for Rock
    #P for Paper
    #S for Scissors
    #u for User 
    #c for Computer
    n=int(input("enter a random number from user:"))
    if(n>=0 and n<=30):
      u="R"
    elif(n>=31 and n<=70):
      u="P"
    elif(n>=71 and n<=100):
      u="S"
    else:
      print("enter valid number")
    print("The User's choice is:",u)
    m=random.randint(1,100)
    if(m>=0 and m<=30):
      c="R"
    elif(m>=31 and m<=70):
      c="P"
    elif(m>=71 and m<=100):
      c="S"
    print("The Computer's choice is:",c)
    if(u=="R" and c=="P"):
        print("C Win")
        print("U lose")
    if(u=="S" and c=="P"):
        print("U Win")
        print("C lose")
    if(u=="R" and c=="S"):
        print("U Win")
        print("C lose")
    if(u=="P" and c=="S"):
        print("C Win")
        print("U lose")
    if(u=="P" and c=="R"):
        print("U Win")
        print("C lose")
    if(u=="S" and c=="R"):
        print("C Win")
        print("U lose")
    elif(u=="S" and c=="S" or u=="R" and c=="R" or u=="P" and c=="P"):
        print("It's a tie")
    k=input("continue the game(yes/no):")
    if(k!="yes"):
        print("Thanks for playing!!")
        break
