import cv2

# Read image
img = cv2.imread("pcb.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect edges
edges = cv2.Canny(gray, 100, 200)

# Display images
cv2.imshow("Original", img)
cv2.imshow("Grayscale", gray)
cv2.imshow("Canny Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()