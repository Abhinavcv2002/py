# create a new datebase
import sqlite3
con=sqlite3.connect('new.db')
try:
    con.execute('create table u_details(user_id int,user_name text,user_phone number int)')#---------# Table creating method
except:
    pass
# con.execute('insert into u_details(user_id,user_name,user_phone) values(1,"abhi",7854201111065)')#-# inserting details into Table
# con.execute('delete from u_details where user_id=3')#----------------------------------------------# delete method
# con.execute('update from u_details ')
# data=con.execute('select * from u_details')#-------------------------------------------------------# Table inserted values display in Terminal
# data=con.execute('select * from u_details where user_id=1')#---------------------------------------# Table one user id displayed in Terminal
# data=con.execute('select count(*) from u_detai ls')
# data=con.execute('select sum(user_id) from u_details')#----------------------------------------------# how many rows in the table
# data=con.execute('select min(user_id) from u_details')#----------------------------------------------# min student in the table
# data=con.execute('select max(user_id) from u_details')#----------------------------------------------# max student in the Table
for i in data:
    # print("{:<2} {:<5} {:<5} " .format(i[0], i[1], i[2], ))#-----------------------------------------# printing the tuple method
    print(i)
con.commit()
