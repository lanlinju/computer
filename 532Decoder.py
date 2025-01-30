# coding=utf-8

import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '532decoder.bin')

with open(filename, 'wb') as file:
    for var in range(32):
        value = 1 << var
        result = value.to_bytes(4, byteorder='little')
        file.write(result)
        
# 00000000000000000000000000000001  offset 0
# 00000000000000000000000000000010  offset 1
# 00000000000000000000000000000100  offset 2
# 10000000000000000000000000000000  offset 31
