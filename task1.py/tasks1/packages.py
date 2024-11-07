import datetime

x=datetime.datetime.now()
print(x)
print(x.strftime("%B"))          #Month name,full version
print(x.strftime("%a"))          #Weekday,short version
print(x.strftime("%A"))          #Weekday,full version
print(x.strftime("%b"))          #Month name,short version 
