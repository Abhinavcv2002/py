#create a 5 multiplication table and print the out in another text

a=int(input("Enter the number :"))
f=open("/home/synnefo/Desktop/py/task1/builin function/Mul work\mul.txt","w")
for i in range(1,11):
    print(i,'*',a,'=',i*a)
    f.write(str(i)+"*"+str(a)+"="+str(i*a)+'/n')