from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load and convert to RGB
image = Image.open("D:/DataAnalysis/Data-Analysis/FPGA_TEST/image.jpeg").convert("RGB")
pixels = np.array(image)

# Flatten pixels to (num_pixels, 3)
flat_pixels = pixels.reshape(-1, 3)

# Combine RGB into a single intensity per pixel (grayscale)
intensity = np.mean(flat_pixels, axis=1)  # or use weighted formula for luminance
#write to binary file
MAX_BYTES = 128 * 1024  # 128 KB
data_to_bytes = intensity.tobytes()[:MAX_BYTES]
with open("D:/DataAnalysis/Data-Analysis/FPGA_TEST/wave_data.bin", "wb") as f:
    f.write(data_to_bytes)
print("Wave saved to 'wave_data.bin'")

# Plot the intensity wave
"""
plt.figure(figsize=(15, 5))
plt.plot(intensity, color='gray')
plt.title('Combined RGB Intensity Wave')
plt.xlabel('Pixel Index')
plt.ylabel('Intensity (0-255)')
plt.tight_layout()
plt.show()"""