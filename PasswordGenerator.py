import string
import random
n=int(input("enter length of password:"))
char=""
while(True):
    c=int(input("enter the choice of characters:"))
    if(c==1):
        char+=string.ascii_letters
    elif(c==2):
        char+=string.digits
    elif(c==3):
        char+=string.punctuation
    elif(c==4):
        break
    else:
        print("enter a valid no.")
password=[]
for i in range(n):
    randchar=random.choice(char)
    password.append(randchar)
print("Random Password is ","".join(password))

