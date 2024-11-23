from add import add
from sub import sub
from mul import mul
from div import div
from numbers import number
while True:
    print(''' 
          1.Addition
          2.Subtract
          3.Multiplication
          4.Division
''')
    choice=int(input("enter the number :"))
    
    if choice == 1:
        a,b=number()
        add(a,b)
    elif choice==2:
        a,b=number()
        sub(a,b)
    elif choice==3:
        a,b=number()
        mul(a,b)
    elif choice==4:
        a,b=number()
        div(a,b)
    elif choice==5:
        break
    else:
        print("invalid")