from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import struct


FILE_PATH = "D:/DataAnalysis/Data-Analysis/sinewave_rgb_image.png"
OUTPUT_PATH = "D:/DataAnalysis/Data-Analysis/out/"
SCALE = 30000.0
CUTOFF = 130
CSV_PATH = "D:/DataAnalysis/Data-Analysis/out/"
def waveform_test(amps):
    waveform = np.array(amps)
    new_waveform = np.zeros(0)
    for i in range(0,1010):
        new_waveform = np.concatenate([new_waveform, waveform])
    return new_waveform

def scale_waveform(pixel_array):
    pixel_array = pixel_array.flatten()
    #Scale all red pixels to negative if < 130 or positive if > 130
    pixel_array = np.array(pixel_array)
    pixel_scaled = np.where(pixel_array > CUTOFF, pixel_array * (SCALE/255.0), pixel_array * (-SCALE/255.0))
    pixel_scaled = pixel_scaled.astype(np.int16)
    return pixel_scaled

try:
    image = Image.open(FILE_PATH)
    image = image.convert("RGB")
    width, height = image.size
    print("Image opened successfully.")
    pixels = np.array(image)
    red_pixels = pixels[:, :, 0]
    green_pixels = pixels[:, :, 1]
    blue_pixels = pixels[:, :, 2]
except FileNotFoundError:
    print("Image file not found. Please check the file path.")

red_scaled = scale_waveform(red_pixels)
green_scaled = scale_waveform(green_pixels)
blue_scaled = scale_waveform(blue_pixels)
# for i in range(10):
#     red_multiple = np.concatenate([red_multiple, red_scaled]).astype(np.int16)

#save to bin file
with open(OUTPUT_PATH + "sin_red_negative_values.bin", "wb") as f:
    for sample in red_scaled:
        f.write(struct.pack('<h', sample))

with open(OUTPUT_PATH + "sin_green_negative_values.bin", "wb") as f:
    for sample in green_scaled:
        f.write(struct.pack('<h', sample))

with open(OUTPUT_PATH + "sin_blue_negative_values.bin", "wb") as f:
    for sample in blue_scaled:
        f.write(struct.pack('<h', sample)) 

np.savetxt(CSV_PATH + "sin_red_csv.csv", red_scaled, delimiter=',')
np.savetxt(CSV_PATH + "sin_green_csv.csv", green_scaled, delimiter=',')
np.savetxt(CSV_PATH + "sin_blue_csv.csv", blue_scaled, delimiter=',')

print(len(red_pixels))
print(len(green_pixels))
print(len(blue_pixels))
