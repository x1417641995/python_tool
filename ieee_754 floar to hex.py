
import struct

'''
this file transform float to hex by ieee_754

@author Ta-Ju
@version 2020-07-08
'''
# float to hex
def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])
# ieee_754 fomat   
def ieee_754(num):
    hexnum = []
    a = float_to_hex(num)
    hexnum.append(int(a[0:4], 16))
    for i in range(4, len(a), 2):
        b = "0x"+a[i:i+2]
        hexnum.append(int(b, 16))
    
    if(num == 0):
        hexnum = [0, 0, 0, 0]
    return hexnum

if __name__ == '__main__':

    print(ieee_754(1.23))