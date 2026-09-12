import cv2

image = cv2.imread("lab-1/images/color.jpg")

if image is None:
    print("Image not found")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


_, black_and_white = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Black and White", black_and_white)

cv2.imwrite("lab-1/images/black_and_white.jpg", black_and_white)

cv2.waitKey(0)
cv2.destroyAllWindows()