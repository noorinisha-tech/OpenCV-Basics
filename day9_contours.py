import cv2

# Read image
img = cv2.imread("shapes.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply threshold
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Find contours
contours, hierarchy = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Draw contours
cv2.drawContours(img, contours, -1, (0,255,0), 2)

# Draw bounding boxes
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)

    # Calculate area
    area = cv2.contourArea(cnt)
    print("Area:", area)

print("Number of objects:", len(contours))

cv2.imshow("Area Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()