# def math():
#     a=1
#     b=2
#     c=3
#     return a,b,C
#     number=math()
#     x,y,z=math():
#     print(number)

#-----------------------------------------------------------------------------#
# function with posstional argument

# def std(name,age):
#     print(name,age)
# std("abhi",21)

#-----------------------------------------------------------------------------#

# function with key word argument

# def std(name,age):
#     print(name,age)
# std(age=21,name="abhi")

#-----------------------------------------------------------------------------#

# function with arbitary argument

# def std(*arg):
#     print(arg)

# std("abhinav",21,"kozhikode")
# std("jerrin","tissur")

#-----------------------------------------------------------------------------#

# function with default parameter Value

# def std(name,age,course="python"):
#     print(name,age,course)

# std("Adharsh",21,"javasciprt")
# std("abhi",21)

#-----------------------------------------------------------------------------#

#function with arbitary keyword argument

# def std(**arg):
#     print(arg)
# std(Name="vinayak",age=22,place="kozhikode")
# std(name="jayalakshmi",place="trissur")
# std(name="abhinesh",age=24,place="trissur")

#-----------------------------------------------------------------------------#

# lambda argument:expression

# add=lambda a,b:a+b
# print(add (5,6))

#-----------------------------------------------------------------------------#

#Build in functions
#map (function,itrable)

# l=[1,2,3,4]
# res=map(lambda a:a*a,l)
# print(list(res))

#def method                   sqaure methods
 
a=[1,2,3,4]
def sqaure(x):
    return x*x
res=list(map(sqaure,a))
print(res)

#-----------------------------------------------------------------------------#
