import cv2

# Read image
img = cv2.imread("shapes.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Otsu's Thresholding
_, otsu = cv2.threshold(
    gray,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# Display
cv2.imshow("Original", img)
cv2.imshow("Grayscale", gray)
cv2.imshow("Otsu Threshold", otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()