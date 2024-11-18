#split

# import re
# a="welcome to all"
# print(re.split('\s',a))

#-------------------------------------------------#
#input charater to remove

# import re
# a="welcome to koachi"
# print(re.split('a',a))

#removed the 'a' character

#-------------------------------------------------#
#input character to change

# import re
# a=" welcome to kochi"
# print(re.sub('to','TO',a))

#'to' character is changed the 'TO'

#-------------------------------------------------#
#input character are counting

# import re
# a="welcome to kochi to"
# print(re.findall('to',a))


#-------------------------------------------------#
#input value of 'o' position checking

# import re
# a="welcome to kochi"
# res=re.search('o',a)
# print(res)

#-------------------------------------------------#
#

# import re
# a="welcome to kochi"
# res=re.search('W',a)
# print(res)

#-------------------------------------------------#
#oru character mathi print

# import re
# a="w"
# res=re.search('w.*',a)#is there 0 or any character after
# print(res)

#-------------------------------------------------#
#'l' after the all character are count

# import re
# a="welcome"
# res=re.search('l.+',a)
# print(res)

#-------------------------------------------------#
#

# import re 
# a="welcome"
# res=re.search('w.?',a)
# print(res)
#-------------------------------------------------#
#the smallest number is checking

# import re
# a="welcome"
# res=re.search('[a-z]',a)
# print(res)

#-------------------------------------------------#
#is there 0-9 or any  after

# import re
# a="welcom9e"
# res=re.search('[0-9]',a)
# print(res)
#-------------------------------------------------#
#all intiger and character are checked

# import re
# a="10"
# res=re.search('[A-Za-z0-9]',a)
# print(res)
#-------------------------------------------------#
#the [A-Z][a-z][0-9] method is followed

import re 
a="Aa2"
res=re.search('[A-Z][a-z][0-9]',a)
print(res)