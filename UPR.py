#realtimefirebase_2 ver.
#
#
print("\n*\n*\n*\nUPR Activated")
from result_class import res3
#import app
#from app import pushdata


import sys
import os

def init():
    import init
    print("\n\n0. START Scanning Image \n")
    init.function()

def module_one():
    import module1
    print("\n\n1. START module 1\n")
    module1.function()

def module_two():
    import module2
    print("\n\n2. START module 2\n")
    module2.function2()
#
def module_three():
    import module3
    print("\n\n3. START module 3\n")
    module3.function3()


def module_four():
    import module4
    print("\n\n4. START module 4\n")
    module4.function4()

import time

init()
start = time.time()
module_one()
if(not res3.isBottle): #isBottle  = False
    pass
else: #isBottle = true
    module_three()
    if(not res3.hasLabel): #hasLabel = false
        module_two()
        if(res3.hasFigure):#hasFigure = true
            pass
        else: #hasFigure = false
            module_four()
    else: #hasLabel = true
        res3.hasFigure = True
        module_four()

res3.calculate_result()
res3.print_final_result()

end = time.time()

pushdata(res3.final_result)
print("\n\n>> Result of module 1 && 2 && 3 && 4=>  "+str(res3.final_result))
print("\n\n>> Duration:" +str(end - start))
print()
