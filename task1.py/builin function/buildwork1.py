#find letter in list using forloop
# a=['apple','orange','kiwi']
# for i in a:
#     if "a" in i:
#         print(i)

#-----------------------------------------------------------------#

#find letter in list using lambda

l=['apple','orange','kiwi','mango']
letter=input("enter the letter :")

print(list(filter(lambda a:letter in a,l)))

#another way lambda

# data=filter(lambda a:letter in a,l)
# print(list(data))