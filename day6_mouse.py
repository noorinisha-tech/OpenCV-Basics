import cv2
import numpy as np

# Create a white image
img = np.ones((500, 500, 3), dtype="uint8") * 255

# Mouse callback function
def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Mouse Clicked at:", x, y)

        # Draw a filled red circle where you click
        cv2.circle(img, (x, y), 10, (0, 0, 255), -1)

        # Update the window
        cv2.imshow("Mouse Events", img)

# Create a window
cv2.namedWindow("Mouse Events")

# Connect the mouse to the window
cv2.setMouseCallback("Mouse Events", mouse_event)

# Display the image
cv2.imshow("Mouse Events", img)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()