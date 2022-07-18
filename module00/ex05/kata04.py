 # Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)
# desired output: module_00, ex_04 : 132.42, 1.00e+04, 1.23e+04

import os
# list of files in the parent directory
arr_pd = os.listdir('..')
# list of files in 2 levels up directory 
# (only those starting with 'm' (just modules))
arr_ppd = [i for i in os.listdir('../..') if i[0] == 'm']
a = arr_ppd[kata[0]]
b = arr_pd[kata[1] - 1]
c = round(kata[2], 2)
d = "{:.2e}".format(kata[3])
e = "{:.2e}".format(kata[4])
print("{}, {} : {}, {}, {}".format(a, b, c, d, e))