from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import struct
import math
SCALE = 30000.0
AMPLITUDE = 255.0
samples_per_symbol = 24
amplitude_threshold = 1.9
image_width = 32
image_height = 32 

# Load and scale a single channel
def load_channel(file_path):
    waveform = np.fromfile(file_path, dtype=np.int16)
    
    waveform = waveform.astype(np.float32) * (AMPLITUDE / SCALE) * 1.85

# Apply correction: if value > 255, subtract value % 255
    waveform = np.where(
        waveform > 255,
        waveform - ((waveform % 255) * 1.85),
        waveform
    )

    # Find valid start (you might refine this condition)
    start_index = 0
    for i in waveform:
        if i > 20:
            start_index = np.where(waveform == i)[0][0]
            break
        
    end_index = start_index + (image_width * image_height)
    print(start_index, end_index)
    pixel_values = waveform[start_index:end_index]
    return pixel_values.astype(np.uint8).reshape((image_height, image_width))

red = load_channel("D:/DataAnalysis/Data-Analysis/captures/sin_red_capture.bin")
green = load_channel("D:/DataAnalysis/Data-Analysis/captures/sin_green_capture.bin")
blue = load_channel("D:/DataAnalysis/Data-Analysis/captures/sin_blue_capture.bin")



image = Image.open("D:/DataAnalysis/Data-Analysis/sinewave_rgb_image.png")
image = image.convert("RGB")
print("Image opened successfully.")
pixels = np.array(image)
red_pixels = pixels[:, :, 0]
green_pixels = pixels[:, :, 1]
blue_pixels = pixels[:, :, 2]

for i in range(1):
    for j in range(image_width):
        print(f"captured: {red[i][j]} ,  {green[i][j]} , {blue[i][j]} ")
        print(f"original: {red_pixels[i][j]} ,  {green_pixels[i][j]} , {blue_pixels[i][j]} ")
        print("--------------------------------------------------")
rgb_image = np.stack((red, green, blue), axis=2)  
image = Image.fromarray(rgb_image, mode='RGB')

# Save
image.save("combined_rgb_image.png")
# with open("Decoded_Flat_Data_Capture.txt", "w") as f:
#     for i in waveform:
#         for j in i:
#             f.write(str(j) + " ")
#         f.write("\n")