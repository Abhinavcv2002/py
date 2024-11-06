                    
                     #importing another file

#-----------------------------------------------------------------------------#
                     #Another way (1st way)

# from functools import reduce
# import tools 
# l=[1,2,3,4,5]
# res=reduce(lambda x,y:x+y,l)
# print(res)

# tools.func1()
# tools.func2()

#-----------------------------------------------------------------------------#

                     #Another way (2nd way)

# from functools import reduce
# import tools as p
# l=[1,2,3,4,5]
# res=reduce(lambda x,y:x+y,l)
# print(res)

# p.func1()
# p.func2()

#-----------------------------------------------------------------------------#

                     #Another way (3rd way)

# from tools import func1,func2

# func1()
# func2()

#-----------------------------------------------------------------------------#

                     #Another way (4th way)

# from tools import *

# func1()
# func2()