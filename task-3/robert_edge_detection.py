import cv2
import numpy as np

image = cv2.imread("Lab-1/images/avengers.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: avengers.jpg not found.")
    exit()

cv2.imshow("Original Image", image)

# Convert to float for calculations
image = image.astype(np.float32)

rows, columns = image.shape

# Create empty derivative images
gx = np.zeros((rows, columns), dtype=np.float32)
gy = np.zeros((rows, columns), dtype=np.float32)

# Roberts Cross Operator
#
# Gx = [ 1   0 ]
#      [ 0  -1 ]
#
# Gy = [ 0   1 ]
#      [-1   0 ]

gx[:-1, :-1] = image[:-1, :-1] - image[1:, 1:]

gy[:-1, :-1] = image[:-1, 1:] - image[1:, :-1]

# Gradient magnitude
edge = np.sqrt((gx ** 2) + (gy ** 2))


# Convert for display
gx = np.clip(np.abs(gx), 0, 255).astype(np.uint8)
gy = np.clip(np.abs(gy), 0, 255).astype(np.uint8)
edge_display = np.clip(edge, 0, 255).astype(np.uint8)

# Display
cv2.imshow("Roberts Gx", gx)
cv2.imshow("Roberts Gy", gy)
cv2.imshow("Roberts Edge", edge_display)

# Save
cv2.imwrite("roberts_edge.png", edge_display)

cv2.waitKey(0)
cv2.destroyAllWindows()