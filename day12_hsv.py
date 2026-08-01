import cv2

# Read image
img = cv2.imread("pcb.jpg")

# Convert BGR image to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define HSV range
lower = (0, 50, 50)
upper = (30, 255, 255)

# Create mask
mask = cv2.inRange(hsv, lower, upper)

# Extract selected color
result = cv2.bitwise_and(img, img, mask=mask)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("HSV Image", hsv)
cv2.imshow("Mask", mask)
cv2.imshow("Selected Color", result)

cv2.waitKey(0)
cv2.destroyAllWindows()