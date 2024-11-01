        # DICTIONARY

#not index
#collection of items as key value pairs
#duplicate values are allowed @ duplicate keys are not allowed
#immutable

# empty dictionary

      # d={}

# d={'key':"value"}
# d={'name':"abhi"}

# d={}


# d={name:'akhil'}
# d['name']='manu'

# Dict = {1: 'abhi', 2: 'vinayak', 3: 'akshay'}
# print(Dict)

#--------------------------------------------------------------------------------------------------#

# List to dictionary convert

# l=["name","age","place"]
# d=dict.fromkeys(l,'null')
# print(d)

#--------------------------------------------------------------------------------------------------#

#update method

# d= {1: 'abhi', 2: 'vinayak', 3: 'akshay'}
# print(d)
# d.update({'1':'manu'})

# limit=int(input("enter the limit"))
# students=[] 
# for i in range(1,limit+1):
#     print('students :',i)
#     sname=input("enter the student name :")
#     sage=input("enter the age :")
#     sroll=input("enter the rollno :")
#     students.append({'name':sname,'age':sage,'roll':sroll})
# print(students)
#---------------------------------------------------------------------------------------------------#
                    # Errors in python
                    # 1.NameError
                    # 2.TypeError
                    # 3.AttributeError
                    # 4.SyntaxError
                    # 5.ValueError
                    # 6.IndexError
                    # 7.IndentationError
                    # 8.ZeroDivisionError
                    # 9.FileNotFoundError
                    # 10.KeyError

#---------------------------------------------------------------------------------------------------#

# Exceptional handling

# try:- her we usualy write the code which would be a error
# except:-
# else:-
# finally:-

#---------------------------------------------------------------------------------------------------#

# example of try and except

# d=[1,2,3,'suhef',22.3]
# sum=0
# for i in (d):
#     try:
#         sum+=i
#     except:
#         pass
# print(sum)

#---------------------------------------------------------------------------------------------------#

# def my_function():
#   print("hlo guys im noob ")
# my_function()

#---------------------------------------------------------------------------------------------------#

# Argument 

# def add(x,y): #formal argument
#     c=x+y
#     print(c)

# a=int(input("enter the number"))
# b=int(input("enter the number"))
# add(a,b) |#actual argument

#---------------------------------------------------------------------------------------------------#

# Return statement

# def add(x,y):
#     c=x+y
#     return c
# a=int(input("enter the number"))
# b=int(input("enter the number "))
# sum=add(a,b)
# print(sum)

#---------------------------------------------------------------------------------------------------#

# calculater
x=int(input("enter 1st number"))
y=int(input("enter 2nd number"))

def add(x,y):
    c=x+y
    return c
def sub(x,y):
    c=x-y
    return c
def mul(x,y):
    c=x*y
    return c
print("""
         1.addition
         2.subraction
         3.multiplication
      
      """)
sum=add(1)
print(sum)
sum=sub(2)
print(sum)
sum=mul(3)
print(sum)

sum=int(input("enter your choice"))


#---------------------------------------------------------------------------------------------------#
