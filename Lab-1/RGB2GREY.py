
import cv2
import numpy as np

image = cv2.imread("lab-1/images/color.jpg")

B = image[:, :, 0]
G = image[:, :, 1]
R = image[:, :, 2]

gray = 0.299 * R + 0.587 * G + 0.114 * B

gray = gray.astype(np.uint8)

cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)

cv2.imwrite("lab-1/images/grey.jpg", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()