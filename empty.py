
import os

'''
this check if txt is empty

@author Ta-Ju
@version 2020-08-20
'''

# load txt
size = os.path.getsize("1.txt")

if(size == 0):
    print("is empty")
else:
    print("not empty")