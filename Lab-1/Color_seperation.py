import cv2

image = cv2.imread("Lab-1/color.jpg")

# Blue image
blue_image = image.copy()
blue_image[:, :, 1] = 0  # Remove Green
blue_image[:, :, 2] = 0  # Remove Red

# Green image
green_image = image.copy()
green_image[:, :, 0] = 0  # Remove Blue
green_image[:, :, 2] = 0  # Remove Red

# Red image
red_image = image.copy()
red_image[:, :, 0] = 0  # Remove Blue
red_image[:, :, 1] = 0  # Remove Green

# Display all images
cv2.imshow("Original", image)
cv2.imshow("Blue Image", blue_image)
cv2.imshow("Green Image", green_image)
cv2.imshow("Red Image", red_image)

cv2.imwrite("output_blue.jpg", blue_image)
cv2.imwrite("output_green.jpg", green_image)
cv2.imwrite("output_red.jpg", red_image)

cv2.waitKey(0)
cv2.destroyAllWindows()