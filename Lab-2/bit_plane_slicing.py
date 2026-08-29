import cv2
import numpy as np

image = cv2.imread("Lab-1/images/color.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: color.jpg not found.")
    exit()

cv2.imshow("Original Image", image)

for bit in range(8):

    plane = ((image // (2 ** bit)) % 2) * 255
    plane = plane.astype(np.uint8)

    cv2.imshow(f"Bit Plane {bit}", plane)

    cv2.imwrite(f"bit_plane_{bit}.png", plane)

    print(f"Saved: bit_plane_{bit}.png")

cv2.waitKey(0)
cv2.destroyAllWindows()