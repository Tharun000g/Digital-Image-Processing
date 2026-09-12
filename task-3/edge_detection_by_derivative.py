import cv2
import numpy as np

image = cv2.imread("Lab-1/images/vortex.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: vortex.jpg not found.")
    exit()

cv2.imshow("Original Image", image)

rows, columns = image.shape

print(f"Image dimensions: {rows} rows x {columns} columns")

# Convert to float so subtraction does not cause uint8 overflow
image = image.astype(np.float32)

# X-direction derivative
x_derivative = np.zeros((rows, columns), dtype=np.float32)
x_derivative[:, :-1] = image[:, 1:] - image[:, :-1]

# Y-direction derivative
y_derivative = np.zeros((rows, columns), dtype=np.float32)
y_derivative[:-1, :] = image[1:, :] - image[:-1, :]

# Absolute values
x_edge = np.abs(x_derivative)
y_edge = np.abs(y_derivative)

# Combine X and Y derivatives
edge = np.sqrt((x_derivative ** 2) + (y_derivative ** 2))

# Threshold level
level = 5

# Show only edges greater than the level
threshold_edge = np.zeros((rows, columns), dtype=np.uint8)
threshold_edge[edge > level] = 255

# Convert edge images to uint8 for display
x_edge = np.clip(x_edge, 0, 255).astype(np.uint8)
y_edge = np.clip(y_edge, 0, 255).astype(np.uint8)
display_edge = np.clip(edge, 0, 255).astype(np.uint8)

# Display results
cv2.imshow("X Direction Edge", x_edge)
cv2.imshow("Y Direction Edge", y_edge)
cv2.imshow("Overall Edge", display_edge)
cv2.imshow("Threshold Edge", threshold_edge)

# Save results
cv2.imwrite("x_edge.png", x_edge)
cv2.imwrite("y_edge.png", y_edge)
cv2.imwrite("edge.png", display_edge)
cv2.imwrite("threshold_edge.png", threshold_edge)

cv2.waitKey(0)
cv2.destroyAllWindows()