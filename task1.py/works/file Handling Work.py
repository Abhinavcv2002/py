#------------------------------------------------------------------------------------------#

try:
    a=open('/home/synnefo/Desktop/py/task1.py/works/file Handling Work.txt','x')
except:
    pass

a=open('/home/synnefo/Desktop/py/task1.py/works/file Handling Work.txt','w')
limit=int(input("enter the limit"))
for i in range(limit):
    names=input("enter the students name")
    a.write(names)
    a.write("\n")

#------------------------------------------------------------------------------------------#

# try:
#     a=open('/home/synnefo/Desktop/py/task1.py/works/file Handling Work.txt','x')
# except:
#     pass

# a=open('filehandling.txt','w')
# limit=int(input("enter the limit"))
# for i in range(limit):
#     name=input("enter the name")
#     a.name(name)
#     a.
