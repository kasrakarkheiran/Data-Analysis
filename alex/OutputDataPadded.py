from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import struct
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('TkAgg')


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

def stretch_waveform(waveform, factor=10):
    return np.repeat(waveform, factor)

def repeat_waveform(waveform, times=3):
    return np.tile(waveform, times)

def repeat_waveform_flipped(waveform):
    flipped = -1 * waveform
    return np.concatenate([waveform, flipped])

def zero_center_waveform(waveform):
    mean_val = np.mean(waveform)
    return waveform - mean_val

red_scaled = scale_waveform(red_pixels)
green_scaled = scale_waveform(green_pixels)
blue_scaled = scale_waveform(blue_pixels)

#stretch each waveform
red_scaled = stretch_waveform(red_scaled, factor=1)
green_scaled = stretch_waveform(green_scaled, factor=1)
blue_scaled = stretch_waveform(blue_scaled, factor=1)

#repeat each waveform
red_scaled = repeat_waveform(red_scaled, times=10)
green_scaled = repeat_waveform(green_scaled, times=10)
blue_scaled = repeat_waveform(blue_scaled, times=10)

#add flipped waveform
#repeat and flip each waveform
#red_scaled = repeat_waveform_flipped(red_scaled)
#green_scaled = repeat_waveform_flipped(green_scaled)
#blue_scaled = repeat_waveform_flipped(blue_scaled)

#zero center the waveform
red_scaled = zero_center_waveform(red_scaled)
green_scaled = zero_center_waveform(green_scaled)
blue_scaled = zero_center_waveform(blue_scaled)

#ensure integer format
red_scaled = red_scaled.astype(np.int16)
green_scaled = green_scaled.astype(np.int16)
blue_scaled = blue_scaled.astype(np.int16)


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


#debugging plot to visualize waveforms

plt.figure(figsize=(15, 5))

plt.subplot(3, 1, 1)
plt.plot(red_scaled, color='red')
plt.title("Red Channel Waveform")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 2)
plt.plot(green_scaled, color='green')
plt.title("Green Channel Waveform")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 3)
plt.plot(blue_scaled, color='blue')
plt.title("Blue Channel Waveform")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()

#show average amplitude
red_avg_amp = np.mean(red_scaled)
green_avg_amp = np.mean(green_scaled)
blue_avg_amp = np.mean(blue_scaled)

print("average amplitudes:")
print(f"R: {red_avg_amp:.2f}")
print(f"G: {green_avg_amp:.2f}")
print(f"B: {blue_avg_amp:.2f}")
