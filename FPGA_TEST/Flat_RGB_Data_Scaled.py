from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import struct


FILE_PATH = "D:/DataAnalysis/Data-Analysis/FPGA_TEST/black_white_checkerboard.png"
OUTPUT_PATH = "D:/DataAnalysis/Data-Analysis/out/key_image.bin"
SCALE = 30000.0
def waveform_test(amps):
    waveform = np.array(amps)
    new_waveform = np.zeros(0)
    for i in range(0,1010):
        new_waveform = np.concatenate([new_waveform, waveform])
    return new_waveform

sampling_rate = 2.4e9
carrier_frequency = 100e6
amplitude = 5.0
secondary_amplitude = 2.5
samples_per_symbol = 24
samples_to_plot = 4 * samples_per_symbol
amplitude_mod = []


try:
    image = Image.open(FILE_PATH)
    image = image.convert("RGB")
    width, height = image.size
    print("Image opened successfully.")
    pixels = np.array(image)
    red_pixels = pixels[:, :, 0]
    amplitude_mod = [2.5 if pixel < 125 else 5.0 for row in red_pixels for pixel in row ]
except FileNotFoundError:
    print("Image file not found. Please check the file path.")

#wwaveform
#waveform = waveform_test(amplitude_mod)
waveform = np.array(amplitude_mod)
waveform_scaled = (waveform / 5.0 * SCALE).astype(np.int16)
with open(OUTPUT_PATH, "wb") as f:
    for sample in waveform_scaled:
        f.write(struct.pack('<h', sample)) 
print(len(waveform_scaled))
# for i in waveform_scaled:
#     print(i)