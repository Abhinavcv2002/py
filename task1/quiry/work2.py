import sqlite3
con=sqlite3.connect('new1.db')
try:
    con.execute('create table sample(AddmissionNO int,user_name text,user_email text,user_phoneNO int,TotalMark int)')
except:
    pass

con.execute('insert into sample(AddmissionNO,user_name,user_email,user_phoneNO,TotalMark) values(2,"viny","vinu@123",87541235412,31)')


#------------------------------------------------------------------------------------------------#
# for i in range(2):
#     print(i+1)
#     id=i+1
#     name=input("Enter the name :")
#     email=input("Enter the email :")
#     phone=int(input("Enter the phone No :"))
#     mark=int(input("Enter the mark :"))
#     con.execute('insert into sample(?,?,?,?) values(id,name,email,phone,ma)')
#------------------------------------------------------------------------------------------------#


con.commit()