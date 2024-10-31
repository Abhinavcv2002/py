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

limit=int(input("enter the limit"))
students=[]
for i in range(1,limit+1):
    print('students :',i)
    s=input("enter the student name :")
    a=input("enter the age :")
    r=input("enter the rollno :")
    students.append({'name':s,'age':a,'roll':r})
print(students)