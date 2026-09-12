import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("Lab-1/images/color.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: color.jpg not found.")
    exit()

hist = np.zeros(256)

for pixel in image.flatten():
    hist[pixel] += 1

cdf = np.zeros(256)
cdf[0] = hist[0]

for i in range(1, 256):
    cdf[i] = cdf[i - 1] + hist[i]

cdf_min = 0

for value in cdf:
    if value != 0:
        cdf_min = value
        break

total_pixels = image.shape[0] * image.shape[1]

mapping = np.zeros(256, dtype=np.uint8)

for i in range(256):
    mapping[i] = round(
        ((cdf[i] - cdf_min) / (total_pixels - cdf_min)) * 255
    )

equalized = mapping[image]

new_hist = np.zeros(256)

for pixel in equalized.flatten():
    new_hist[pixel] += 1

cv2.imshow("Original Image", image)
cv2.imshow("Equalized Image", equalized)


cv2.imwrite("lab-2/images/equalized.png", equalized)

plt.figure()
plt.title("Original Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.plot(hist)

plt.figure()
plt.title("Equalized Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.plot(new_hist)

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()