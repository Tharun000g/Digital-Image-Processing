'''import cv2

image = cv2.imread("lab-1/color.jpg")

#print(image.shape)

#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("output.png", gray)

#print(gray.shape)
#print(image.shape)

blue = image[:,:,0]
green = image[:, :, 1]



print(type(image))
print(image.shape)
print(image.dtype)
print(image.ndim)
print(image.size)

blue = image[:, :, 0]
green = image[:, :, 1]
red = image[:, :, 2]

print(blue.shape)
print(green.shape)
print(red.shape)

blue_image = image.copy()

blue_image[:, :, 2] = 0
blue_image[:, :, 0] = 0

cv2.imshow("Blue", blue_image)

cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
import numpy as np

image = np.zeros((300, 300), dtype=np.uint8)


image[100:155,100:250]=255
cv2.imshow("Black Image", image)



cv2.waitKey(0)
cv2.destroyAllWindows()



import cv2
import numpy as np

image = cv2.imread("lab-1/color.jpg")

# Make image darker
dark = image.astype(np.int16)
dark = dark // 2
dark = dark.astype(np.uint8)

# Make image brighter
bright = image.astype(np.int16)
bright = bright + 100
bright = np.clip(bright, 0, 255)
bright = bright.astype(np.uint8)

cv2.imshow("Original", image)
cv2.imshow("Dark", dark)
cv2.imshow("Bright", bright)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

image = cv2.imread("lab-1/color.jpg")

crop = image[100:120, 204:450]

small = cv2.resize(image, (40000, 3000))
print((image.size)/1000000)
cv2.imshow("Original", small)
cv2.waitKey(0) '''

