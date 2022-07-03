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
cv2.createTrackbar("GMIN", "Trackbars", 0, 255, nothing)
# create a trackbar for GMAX , start:255 counter:255 callback:nothing
cv2.createTrackbar("GMAX", "Trackbars", 255, 255, nothing)
# create a trackbar for BMIN , start:0 counter:255 callback:nothing
cv2.createTrackbar("BMIN", "Trackbars", 0, 255, nothing)
# create a trackbar for BMAX , start:255 counter:255 callback:nothing
cv2.createTrackbar("BMAX", "Trackbars", 255, 255, nothing)
#### END OF YOUR CODE ####

while True:
    
<<<<<<< HEAD
    # read the image lane.jpg
    image = cv2.imread(dir_path+'/lane.jpg')
=======
    # read the image lane,jpg
>>>>>>> c10ef2e5839e23a395e35dd97336f674e6db72b5
    
    
    rmin = cv2.getTrackbarPos("RMIN", "Trackbars") # get the trackbar position for hue min
    rmax = cv2.getTrackbarPos("RMAX", "Trackbars") # get the trackbar position for hue max

    #### WRITE YOUR CODE HERE ####
    # get the trackbar position for GMIN
    gmin = cv2.getTrackbarPos("GMIN", "Trackbars")
    # get the trackbar position for GMAX
    gmax = cv2.getTrackbarPos("GMAX", "Trackbars")
    # get the trackbar position for BMIN
    bmin = cv2.getTrackbarPos("BMIN", "Trackbars")
    # get the trackbar position for BMAX
    bmax = cv2.getTrackbarPos("BMAX", "Trackbars")

    # create a lower range array
    lower_range = np.array([rmin, gmin, bmin])
    # create a upper range array
    upper_range = np.array([rmax, gmax, bmax])
    # create a mask for the image using inRange , with the lower and upper range array
    mask = cv2.inRange(image, lower_range, upper_range)
    final_result = cv2.bitwise_and(image, image,mask=mask) # create a final result for the image

    # display the mask, final result and the image
    cv2.imshow("Mask", mask)
    cv2.imshow("Final Result", final_result)
    cv2.imshow("Image", image)

    #### END OF YOUR CODE ####
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
