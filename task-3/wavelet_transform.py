import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Lab-1/images/color.jpg", 0)
img = img.astype(float)

rows, cols = img.shape

rows = rows - rows % 2
cols = cols - cols % 2

img = img[:rows, :cols]

low = (img[:, 0::2] + img[:, 1::2]) / np.sqrt(2)
high = (img[:, 0::2] - img[:, 1::2]) / np.sqrt(2)

LL = (low[0::2, :] + low[1::2, :]) / np.sqrt(2)
LH = (low[0::2, :] - low[1::2, :]) / np.sqrt(2)

HL = (high[0::2, :] + high[1::2, :]) / np.sqrt(2)
HH = (high[0::2, :] - high[1::2, :]) / np.sqrt(2)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(LL, cmap="gray")
plt.title("LL - Approximation")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(LH, cmap="gray")
plt.title("LH - Horizontal Detail")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(HL, cmap="gray")
plt.title("HL - Vertical Detail")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(HH, cmap="gray")
plt.title("HH - Diagonal Detail")
plt.axis("off")

plt.tight_layout()

plt.savefig("Lab-1/images/wavelet_transform.jpg")

plt.show()