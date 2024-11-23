
#---------------------------------------------------------------------------------------------------#

#open (file_name,mode)

  #modes
#x-> create
#r-> read
#w->write
#a->append

#---------------------------------------------------------------------------------------------------#

# f=open('/home/synnefo/Desktop/py/task1.py/builin function/arithametic/demo.txt','x')                  #
# f.write('welcome to all')               # 

#---------------------------------------------------------------------------------------------------#

# f=open('/home/synnefo/Desktop/py/task1/builin function/sample.txt','w')                  #over write the text
# f.write(' demo write ')

#---------------------------------------------------------------------------------------------------#

# f=open('/home/synnefo/Desktop/py/task1/builin function/sample.txt','a')                  #append the word in the text
# f.write(' helo world ')

#---------------------------------------------------------------------------------------------------#

# f=open('/home/synnefo/Desktop/py/task1/builin function/sample.txt','a')                  #append the word in the text
# x=[10,20]
# f.write(str(x))

#---------------------------------------------------------------------------------------------------#

# f=open('/home/synnefo/Desktop/py/task1/builin function/demo.txt','r')
# a=f.read()
# a=f.read(10)  #  //The 10 c character are print
# print(a)
# b=f.read()    #  //the 10 after character are print
# print(b)

#---------------------------------------------------------------------------------------------------#

# f=open('/home/synnefo/Desktop/py/task1/builin function/demo.txt','r')
# a=f.readline().strip()
# print(a)
# b=f.readline().strip()
# print(b)

#---------------------------------------------------------------------------------------------------#
#Lines are print

# f=open('/home/synnefo/Desktop/py/task1/builin function/demo.txt','r')
# a=f.readlines()
# print(len(a))

#---------------------------------------------------------------------------------------------------#

# f=open('/home/synnefo/Desktop/py/task1/builin function/demo.txt','r')
# print(f.tell())
# f.seek(0)
# print(f.tell())

#---------------------------------------------------------------------------------------------------#
#reversed string 

# f=open('/home/synnefo/Desktop/py/task1/builin function/demo.txt','r')
# a=f.readlines()
# f.seek(0)
# for i in range(len(a)):
#     b=f.readline().strip()
#     print(b[::-1])

#---------------------------------------------------------------------------------------------------#

# f=open('/home/synnefo/Desktop/py/task1/builin function/demo.txt','r')
# a=f.readlines()
# f.seek(0)
# letter=0
# for i in range(len(a)):
#     b=f.readline()
#     # print(b)
#     for j in b:
#         if j!=' ':
#             letter+=1
# print('letter',letter)

#---------------------------------------------------------------------------------------------------#

f=open('/home/synnefo/Desktop/py/task1/builin function/demo.txt','r')
a=f.readlines()
f.seek(0)
letter=0
for i in range(len(a)):
    b=f.readline()
    # print(b)
    for j in b:
        if j!=' ':
            letter+=1
            print('letter',letter)

            
#---------------------------------------------------------------------------------------------------#
