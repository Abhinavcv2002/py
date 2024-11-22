x=int(input("enter the first number"))
y=int(input("enter the second number"))
z=int(input("enter the third number"))
if(x>y):
    if(x<z):
        print(x,"is largest")
    else:
        print(z,"is largest")
else:
    if(y>z):
        print(y,"is largest")
    else:
        print(z,"is largest")