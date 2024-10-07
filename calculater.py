a=int(input("enter the first number"))
b=int(input("enter the second number"))
print("""
         1.addition
         2.subraction
         3.multiplication
         4.divition
         6.modules
         7.floor division
         8.exponents
         """)
c=int(input("enter the choice"))
if(c==1):
    print(a+b)
elif(c==2):
    print(a-b)
elif(c==3):
    print(a*b)
elif(c==4):
    print(a/b)
elif(c==5):
    print(a%b)
elif(c==6):
    print(a//b)
elif(c==7):
    print(a**b)
else:
    print("invalid")

