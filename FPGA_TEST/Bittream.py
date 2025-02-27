import numpy as np
RANGE = 128000*8
with open('FPGA_TEST/bit.bin', 'wb') as f:
    for i in range(0,RANGE):
        if(i%2 == 0):
            f.write(int.to_bytes(1))
        else:
            f.write(int.to_bytes(0))
    f.close()

        
        