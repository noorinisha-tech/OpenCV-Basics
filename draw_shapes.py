import cv2

# Read the image
img = cv2.imread("car.jpg")

# Draw a rectangle
cv2.rectangle(img, (50, 50), (300, 200), (0, 255, 0), 3)

# Draw a circle
cv2.circle(img, (400, 150), 60, (255, 0, 0), 3)

# Draw a line
cv2.line(img, (50, 250), (500, 250), (0, 0, 255), 3)

# Write text
cv2.putText(img, "OpenCV Day 4", (50, 320),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Save the edited image
cv2.imwrite("edited_car.jpg", img)

# Display the image
cv2.imshow("Edited Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()