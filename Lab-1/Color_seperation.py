import cv2

image = cv2.imread("Lab-1/images/color.jpg")

# Blue image
blue_image = image.copy()
blue_image[:, :, 1] = 0 
blue_image[:, :, 2] = 0 

# Green image
green_image = image.copy()
green_image[:, :, 0] = 0  
green_image[:, :, 2] = 0  

# Red image
red_image = image.copy()
red_image[:, :, 0] = 0  
red_image[:, :, 1] = 0  

# Display all images
cv2.imshow("Original", image)
cv2.imshow("Blue Image", blue_image)
cv2.imshow("Green Image", green_image)
cv2.imshow("Red Image", red_image)



cv2.waitKey(0)
cv2.destroyAllWindows()