import os, sys


'''
this file removefile

@author Ta-Ju
@version 2020-08-20
'''

# print list of index
print ("index: %s" %os.listdir(os.getcwd()))


a = os.listdir(os.getcwd())
# remove file
for i in a:
    if(i != "removefile.py" and i != "removefolder.py" and i != "empty.py"):
        os.remove(i)


# print after remove index
print ("after remove index: %s" %os.listdir(os.getcwd()))