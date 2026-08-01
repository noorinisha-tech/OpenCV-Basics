import cv2

# Read image
img = cv2.imread("pcb.jpg")

# Resize image
resized = cv2.resize(img, (500, 400))

# Rotate image 90 degrees clockwise
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Flip image horizontally
flipped = cv2.flip(img, 1)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", resized)
cv2.imshow("Rotated Image", rotated)
cv2.imshow("Flipped Image", flipped)

cv2.waitKey(0)
cv2.destroyAllWindows()