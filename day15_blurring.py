import cv2

# Read image
img = cv2.imread("pcb.jpg")

# Apply different blurring methods
average = cv2.blur(img, (5, 5))
gaussian = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)

# Display images
cv2.imshow("Original", img)
cv2.imshow("Average Blur", average)
cv2.imshow("Gaussian Blur", gaussian)
cv2.imshow("Median Blur", median)

cv2.waitKey(0)
cv2.destroyAllWindows()