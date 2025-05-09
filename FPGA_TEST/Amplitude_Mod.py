from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import struct
print("Amplitude Modulation")

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


#time vector for a single symbol modulation
t_symbol = np.linspace(0, samples_per_symbol/sampling_rate, samples_per_symbol, endpoint=False)

#waveform of height
height_waveform = height * np.sin(2*np.pi*carrier_frequency*t_symbol)
#waveform of width
width_waveform = width * np.sin(2*np.pi*carrier_frequency*t_symbol)


waveform = np.concatenate([amp * np.sin(2 * np.pi * carrier_frequency * t_symbol) for amp in amplitude_mod])
#total waveform height and width
# waveform = np.concatenate([height_waveform, width_waveform, waveform])
#time vector for the entire waveform
t_waveform = np.linspace(0, len(waveform)/sampling_rate, len(waveform), endpoint=False)
#time vector for the limited waveform
t_limited = np.linspace(0, samples_to_plot/sampling_rate, samples_to_plot, endpoint=False)

# waveform_two = np.array(waveform_two)
# waveform_eight = np.array(waveform_eight)
#voltage ranges from -327mV to 327mV +- some error of around 30mV
waveform_scaled = (waveform / 5.0 * 32767).astype(np.int16)
for i in waveform_scaled:
    print(i)
print(len(waveform_scaled))
# Save to binary file (little-endian int16)
with open("modulated_output_int16.bin", "wb") as f:
    for sample in waveform_scaled:
        f.write(struct.pack('<h', sample)) 


#print(waveform)
# plt.figure(figsize=(10, 4))
# plt.plot(t_limited, waveform[:samples_to_plot])
# plt.title('Sine Wave')
# plt.xlabel('time (s)')
# plt.ylabel('Amplitude (V)')
# plt.grid(True)
# plt.show()