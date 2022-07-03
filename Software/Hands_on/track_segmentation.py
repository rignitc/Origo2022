import cv2
import numpy as np
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def nothing(a): # Required for the trackbar to work
    pass # Do nothing


cv2.namedWindow("Trackbars") # create a window for trackbar
cv2.resizeWindow("Trackbars", 600, 600) # resize the window
cv2.createTrackbar("RMIN", "Trackbars", 0, 255, nothing) # create a trackbar for hue min,start:0 counter:179 callback:nothing
cv2.createTrackbar("RMAX", "Trackbars", 255, 255, nothing) # create a trackbar for hue max,start:179 counter:179 callback:nothing

#### WRITE YOUR CODE HERE ####

# create a trackbar for GMIN , start:0 counter:255 callback:nothing

# create a trackbar for GMAX , start:255 counter:255 callback:nothing

# create a trackbar for BMIN , start:0 counter:255 callback:nothing

# create a trackbar for BMAX , start:255 counter:255 callback:nothing

#### END OF YOUR CODE ####

while True:
    
    # read the image lane,jpg
    
    
    hmin = cv2.getTrackbarPos("RMIN", "Trackbars") # get the trackbar position for hue min
    hmax = cv2.getTrackbarPos("RMAX", "Trackbars") # get the trackbar position for hue max

    #### WRITE YOUR CODE HERE ####
    # get the trackbar position for GMIN

    # get the trackbar position for GMAX

    # get the trackbar position for BMIN

    # get the trackbar position for BMAX

    # create a lower range array

    # create a upper range array

    # create a mask for the image using inRange , with the lower and upper range array
    
    final_result = cv2.bitwise_and(image, image,mask=mask) # create a final result for the image

    # display the mask, final result and the image

    #### END OF YOUR CODE ####
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
