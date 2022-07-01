import cv2
import numpy as np

def nothing(a): # Required for the trackbar to work
    pass # Do nothing


cv2.namedWindow("Trackbars") # create a window for trackbar
cv2.resizeWindow("Trackbars", 600, 600) # resize the window
cv2.createTrackbar("HueMin", "Trackbars", 0, 179, nothing) # create a trackbar for hue min
cv2.createTrackbar("HueMax", "Trackbars", 179, 179, nothing) # create a trackbar for hue max
cv2.createTrackbar("SaturationMin", "Trackbars", 0, 255, nothing) # create a trackbar for saturation min
cv2.createTrackbar("SaturationMax", "Trackbars", 255, 255, nothing) # create a trackbar for saturation max
cv2.createTrackbar("ValueMin", "Trackbars", 0, 255, nothing) # create a trackbar for value min
cv2.createTrackbar("ValueMax", "Trackbars", 255, 255, nothing) # create a trackbar for value min



while True:
    image = cv2.imread("location to lane.jpg")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hmin = cv2.getTrackbarPos("HueMin", "Trackbars") # get the trackbar position for hue min
    hmax = cv2.getTrackbarPos("HueMax", "Trackbars") # get the trackbar position for hue max
    smin = cv2.getTrackbarPos("SaturationMin", "Trackbars")
    smax = cv2.getTrackbarPos("SaturationMax", "Trackbars")
    vmin = cv2.getTrackbarPos("ValueMin", "Trackbars")
    vmax = cv2.getTrackbarPos("ValueMax", "Trackbars")
    lower = np.array([hmin, smin, vmin]) # create a lower range array
    upper = np.array([hmax, smax, vmax]) # create a upper range array
    mask = cv2.inRange(image, lower, upper) # create a mask for the image
    final_result = cv2.bitwise_and(image, image,mask=mask) # create a final result for the image

    cv2.imshow("mask", mask)
    cv2.imshow("image", image)
    cv2.imshow("final_result", final_result)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break