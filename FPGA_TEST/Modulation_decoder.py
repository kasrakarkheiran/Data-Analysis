from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import struct
import math

samples_per_symbol = 24
amplitude_threshold = 2
image_width = 8
image_height = 8  



waveform = np.fromfile("D:/DataAnalysis/Data-Analysis/FPGA_TEST/cap12.bin", dtype=np.int16)
waveform = waveform.astype(np.float32) * (5.0/32767.0)

start_index = 0
end_index = 0

#find where the image starts from
for i in waveform:
    if i > 0.5 or i < -0.5:
        start_index = np.where(waveform == i)[0][0]
        break
print("Start index:", start_index)

# #find where the image ends
# for i in waveform[::-1]:
#     if i > 0.5 or i < -0.5:
#         end_index = len(waveform) - np.where(waveform[::-1] == i)[0][0]
#         break   


end_index = start_index + (image_width * image_height * samples_per_symbol)


#limit waveform to the image data
waveform = waveform[start_index:end_index]
print("Length of waveform:", len(waveform))

#calculate number of symbols, basically the number of pixels in the image
num_symbols = math.ceil(len(waveform) / samples_per_symbol)
#reshape it into a 2D array where rows is each pixel and columns is the samples of that pixel
symbols = waveform[:num_symbols * samples_per_symbol].reshape((num_symbols, samples_per_symbol))

#get the peak amplitude of each pixel
amplitudes = np.max(np.abs(symbols), axis=1)  # peak method

pixel_values = np.where(amplitudes < amplitude_threshold, 0, 255).astype(np.uint8)


image_array = pixel_values.reshape((image_height, image_width))
image = Image.fromarray(image_array, mode='L')  # 'L' means 8-bit grayscale


image.save("reconstructed_checkerboard.png")
image.show()
