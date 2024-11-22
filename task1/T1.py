a=int(input("enter the number"))
if a<=100:
    print("no change")
elif a<=200:
    a=a-100
    cost=a*5
elif a>200:
    a=a-200
    a=(a*10)+500