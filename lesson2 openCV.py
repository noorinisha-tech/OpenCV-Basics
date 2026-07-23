import cv2

# Read the image
img = cv2.imread("car.jpg")

# Print image size
print("Image Shape:", img.shape)

# Resize the image
resized = cv2.resize(img, (500, 300))

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Save the grayscale image
cv2.imwrite("gray_car.jpg", gray)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", resized)
cv2.imshow("Gray Image", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()