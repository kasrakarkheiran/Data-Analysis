from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import struct
print("Amplitude Modulation")




time = 1e-6
sampling_rate = 2.4e9
frequency = 100e6
amplitude = 5.0
secondary_amplitude = 2.5
samples_per_symbol = 24
num_samples = int(sampling_rate * time)




try:
    image = Image.open("D:/DataAnal/Data-Analysis-1/FPGA_TEST/black_white_checkerboard.png")
    image = image.convert("RGB")
    print("Image opened successfully.")
    pixels = np.array(image)
    red_pixels = pixels[:, :, 0]
    new_pixel_values = [[2.5 if pixel == 0 else 5.0 for pixel in row] for row in red_pixels]
except FileNotFoundError:
    print("Image file not found. Please check the file path.")
#time vector
t = np.linspace(0, time, num_samples, endpoint=False)

#generate sinewave
carrier_sine_wave = amplitude * np.sin(2 * np.pi * frequency * t)
print(carrier_sine_wave)
plt.figure(figsize=(10, 4))
plt.plot(t, carrier_sine_wave)
plt.title('Sine Wave')
plt.xlabel('time (s)')
plt.ylabel('Amplitude (V)')
plt.grid(True)
plt.show()