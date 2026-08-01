import cv2

# Read image
img = cv2.imread("pcb.jpg")

# Apply Gaussian Blur
gaussian = cv2.GaussianBlur(img, (5, 5), 0)

# Apply Median Blur
median = cv2.medianBlur(img, 5)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Gaussian Blur", gaussian)
cv2.imshow("Median Blur", median)

cv2.waitKey(0)
cv2.destroyAllWindows()