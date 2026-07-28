import cv2

# Load the image
image = cv2.imread("car.jpg")

# Resize the image
image = cv2.resize(image, (600, 400))

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect edges
edges = cv2.Canny(gray, 100, 200)

# Show images
cv2.imshow("Original Image", image)
cv2.imshow("Gray Image", gray)
cv2.imshow("Canny Edge Detection", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()