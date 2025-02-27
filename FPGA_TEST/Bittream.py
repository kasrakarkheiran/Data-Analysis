import numpy as np
import struct
RANGE = 128000
value = 1
DATA = packed_data = struct.pack("<h", value)

with open('FPGA_TEST/bit.bin', 'wb') as f:
    for i in range (0,65000):
        f.write(DATA)
    f.close()   
        