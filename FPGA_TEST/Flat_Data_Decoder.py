from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import struct
import math
SCALE = 30000.0
AMPLITUDE = 5.0
samples_per_symbol = 24
amplitude_threshold = 1.9
image_width = 8
image_height = 8  



waveform = np.fromfile("D:/DataAnalysis/Data-Analysis/captures/checkerbox_flatdata_capture.bin", dtype=np.int16)
waveform = waveform.astype(np.float32) * (AMPLITUDE/SCALE)
start_index = 0
for i in waveform:
    if i>1:
        start_index = np.where(waveform == i)[0][0]
        break
end_index = start_index + (image_width * image_height)

waveform = waveform[start_index:end_index]

waveform = np.where(waveform > amplitude_threshold, 255, 0).astype(np.uint8)
waveform = waveform.reshape(8,8)
with open("Decoded_Flat_Data_Capture.txt", "w") as f:
    for i in waveform:
        for j in i:
            f.write(str(j) + " ")
        f.write("\n")