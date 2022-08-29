print("\t\t\t\tWelcome to my Calculator !")
print("What you are looking for\n1)Addition(+)\n2)Subtraction(-)\n3)Multiplication(*)\n4)Division(/)")
num=int(input("Enter the operation to Perform:"))
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
def calci(a,b):
    if (num==1):
        print("Addition is " + str(a+b))
    elif(num==2):
        print("Subtraction is " + str(a-b))
    elif(num==3):
        print("Multiplication is " + str(a*b))
    elif(num==4):
        if(b == 0):
            print("Mathmatical Error")    
        else:
            print("Division is "+ str(a/b))
    else:
        print("Typing Error")
calci(a,b)
