import cv2
import numpy as np

# Create a blank white image
img = np.ones((500, 500, 3), dtype="uint8") * 255

# Draw a blue line
cv2.line(img, (50, 50), (450, 50), (255, 0, 0), 3)

# Draw a green rectangle
cv2.rectangle(img, (50, 100), (200, 250), (0, 255, 0), 3)

# Draw a red circle
cv2.circle(img, (350, 175), 60, (0, 0, 255), 3)

# Draw a filled yellow circle
cv2.circle(img, (350, 350), 40, (0, 255, 255), -1)

# Write text
cv2.putText(
    img,
    "OpenCV Day 3",
    (100, 470),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 0, 0),
    2
)

# Show the image
cv2.imshow("Drawing Shapes", img)

# Wait until a key is pressed
cv2.waitKey(0)

# Close the window
cv2.destroyAllWindows()