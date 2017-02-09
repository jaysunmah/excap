import cv2
import numpy as np

window_name = "Webcam!"

cam_index = 0 # Default camera is at index 0.

# Create a window to display to
cv2.namedWindow(window_name, cv2.CV_WINDOW_AUTOSIZE)

cap = cv2.VideoCapture(cam_index) # Video capture object
cap.open(cam_index) # Enable the camera

newFrame = []
# Loop indefinitely
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
