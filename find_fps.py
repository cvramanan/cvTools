# importing libraries
# from time import time
import time
import cv2
import numpy as np

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture(2)

# Check if camera opened successfully
if (cap.isOpened()== False):
    print("Error opening video file")


t = time.time()
# Read until video is completed
while(cap.isOpened()):
	
    # Capture frame-by-frame
    t = time.time()
    ret, frame = cap.read()
    print("Frame: ", 1/(time.time() - t))
    if ret == True:

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release
# the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
