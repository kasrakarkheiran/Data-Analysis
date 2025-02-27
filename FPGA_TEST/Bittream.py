import numpy as np
import struct
RANGE = 128000
value = 3060
DATA = packed_data = struct.pack("<h", value)

with open('FPGA_TEST/bit.bin', 'wb') as f:
    for i in range (0,64000):
        f.write(DATA)
    f.close()   
        