print("\t\t\t\twelcome to my calculator")
print("what you are looking for\n1)addition(+)\n2)subtraction(-)\n3)multiplication(*)\n4)division(/)")
a=int(input("enter first number"))
b=int(input("enter second number"))
num=int(input("enter your choice number"))
def calci(c,d):
    if (num==1):
        print(c+d)
    elif(num==2):
        print(c-d)
    elif(num==3):
        print(c*d)
    elif(num==4):
        print(c/d)
    else:
        print("typing error")
calci(a,b)
