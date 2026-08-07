import cv2

# Read image
img = cv2.imread("shapes.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, hierarchy = cv2.findContours(
    threshold,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Draw contours
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# Display
cv2.imshow("Contours", img)

cv2.waitKey(0)
cv2.destroyAllWindows()