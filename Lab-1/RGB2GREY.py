
import matplotlib.pyplot as plt
import numpy as np

# Read the image
image = plt.imread("lab-1/color.jpg")
print(image.shape)
    
# Get the RGB channels
R = image[:, :, 0]
G = image[:, :, 1]
B = image[:, :, 2]

# Use only the Red channel
gray = R

# Display the grayscale image
plt.imshow(gray, cmap="gray")
plt.imsave("output_red.jpg", gray, cmap="gray")
plt.axis("off")
plt.show()