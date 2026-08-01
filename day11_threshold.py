import cv2

# Read image
img = cv2.imread("shapes.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Binary threshold
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Inverse binary threshold
_, binary_inv = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Otsu thresholding
_, otsu = cv2.threshold(
    gray, 0, 255,
    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
)

# Adaptive thresholding
adaptive = cv2.adaptiveThreshold(
    gray,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV,
    11,
    2
)

# Display
cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("Binary Threshold", binary)
cv2.imshow("Inverse Binary", binary_inv)
cv2.imshow("Otsu Threshold", otsu)
cv2.imshow("Adaptive Threshold", adaptive)

cv2.waitKey(0)
cv2.destroyAllWindows()