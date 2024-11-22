#SUM OF THE NATURAL AND EVEN AND ODD NUMBER
nsum=0
esum=0
osum=0
i=1
while(i<=10):
    nsum+=i
    if(i%2==0):
        esum+=i
    elif(i%2==1):
        osum+=i
    else:
        pass
    i+=1
print("sum of natural number :",nsum)
print("sum of even number :",esum)
print("sum of odd number :",osum)