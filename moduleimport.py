#  importing expression and Lambda module(file) in this file


from expression import *
show()
disp()
arithmetics()

from Lambda import *


#    =======  or  ==============

import function
function.disp()
function.add(12,33)



#      or       ..........


import function as f
f.disp()
f.add(11,44)


#  to know current working directory  .........


import os
os.getcwd()