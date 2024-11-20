import re 
pattern="^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[@#$%^&+=]).*$"
password=input("enter the : ")
result=re.findall(pattern, password)
if(result):
    print("valid password")
else:
    print("password not valid")