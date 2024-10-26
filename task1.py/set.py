       #SET DATA TYPE

    #add method
# s=set()
# s.add(1)
# print(s)

#----------------------------------------------------------------------------------------------------------#
    #update method
# s=set()
# s.add(2)
# s.update({1,3})
# print(s)

#----------------------------------------------------------------------------------------------------------#
    #pop method
# s={1,2,3,4}
# s.pop()
# print(s)

#----------------------------------------------------------------------------------------------------------#
    #remove method
# s={1,2,3,4}
# s.remove(3)
# print(s)

#----------------------------------------------------------------------------------------------------------#
    #discard method
# s={1,2,3,4}
# s.discard(3)
# print(s)

#----------------------------------------------------------------------------------------------------------#
   
# s1={1,2,3,8}
# s2={1,2,3,4,5,6}

# print(s2.difference(s1))                   #difference method
# print(s2.intersection(s1))                 #intersection method
# print(s2.isdisjoint(s1))                   #isdisjoint method
# print(s2.issubset(s1))                     #issubset method
# print(s2.issuperset(s1))                   #issuperset method
# s2=s1.copy()
# s2.difference_update(s1)                   #difference_update method
# print(s2)
# s2.intersection_update(s1)                 #intersection update method
# print(s2)
# s2.symmetric_difference_update(s1)         #symmetricdifference_update method
# print(s2)

#----------------------------------------------------------------------------------------------------------#