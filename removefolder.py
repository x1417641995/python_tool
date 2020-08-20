import os, sys

import shutil  

'''
this file removefolder

@author Ta-Ju
@version 2020-08-20
'''

# print list of index
print ("目录为: %s" %os.listdir(os.getcwd()))

# remove folder

shutil.rmtree('__pycache__')

# print after remove index
print ("移除后 : %s" %os.listdir(os.getcwd()))