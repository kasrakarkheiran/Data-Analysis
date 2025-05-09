from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import struct


FILE_PATH = "D:/DataAnalysis/Data-Analysis/FPGA_TEST/black_white_checkerboard.png"
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
    amplitude_mod = [2.5 if pixel == 0 else 5.0 for row in red_pixels for pixel in row ]
except FileNotFoundError:
    print("Image file not found. Please check the file path.")

#wwaveform
waveform = np.array(amplitude_mod)
waveform_two = []
waveform_eight = []
for j in amplitude_mod:
    for i in range(0,4):
        waveform_two.append(j)

for j in amplitude_mod:    
    for i in range(0,8):
        waveform_eight.append(j)

waveform_scaled = (waveform / 5.0 * 32767).astype(np.int16)
with open("modulated_output_with_repeats.bin", "wb") as f:
    for sample in waveform_scaled:
        f.write(struct.pack('<h', sample)) 