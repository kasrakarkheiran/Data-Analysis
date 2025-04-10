from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import struct

#load test numbers
numbers = []
for i in range(0, 65536):
    numbers.append(i%255)
# Open the file for writing in binary mode
with open('D:/DataAnalysis/Data-Analysis/FPGA_TEST/wave_data.bin', 'wb') as f:
    for num in numbers:
        # '<h' means little-endian ('<') 16-bit signed integer ('h')
        f.write(struct.pack('<h', num))