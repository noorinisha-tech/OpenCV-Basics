import cv2

# Read image
img = cv2.imread("shapes.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Simple binary threshold
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Display
cv2.imshow("Original", img)
cv2.imshow("Grayscale", gray)
cv2.imshow("Threshold", threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()