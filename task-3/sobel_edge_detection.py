import cv2
import numpy as np

image = cv2.imread("Lab-1/images/vortex.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: vortex.jpg not found.")
    exit()

cv2.imshow("Original Image", image)

# Convert to float for calculations
image = image.astype(np.float32)

# Sobel Operators
#
# Gx = [-1  0  1]
#      [-2  0  2]
#      [-1  0  1]
#
# Gy = [-1 -2 -1]
#      [ 0  0  0]
#      [ 1  2  1]

Gx = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
], dtype=np.float32)

Gy = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
], dtype=np.float32)

# Apply Sobel operators
gx = cv2.filter2D(image, -1, Gx)
gy = cv2.filter2D(image, -1, Gy)

# Gradient magnitude
edge = np.sqrt((gx ** 2) + (gy ** 2))

# Convert for display
gx = np.clip(np.abs(gx), 0, 255).astype(np.uint8)
gy = np.clip(np.abs(gy), 0, 255).astype(np.uint8)
edge_display = np.clip(edge, 0, 255).astype(np.uint8)

# Display results
cv2.imshow("Sobel Gx", gx)
cv2.imshow("Sobel Gy", gy)
cv2.imshow("Sobel Edge", edge_display)

# Save results
cv2.imwrite("sobel_gx.png", gx)
cv2.imwrite("sobel_gy.png", gy)
cv2.imwrite("sobel_edge.png", edge_display)

cv2.waitKey(0)
cv2.destroyAllWindows()