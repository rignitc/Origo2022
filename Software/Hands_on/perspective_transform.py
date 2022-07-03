import numpy as np
import cv2
import os
import sys
import random

dir_path = os.path.dirname(os.path.realpath(__file__))
img = cv2.imread(dir_path+'/lane.jpg')
mouseX = 0
mouseY = 0
# print the co-ordinates in the image on mouse click
def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        r =  random.randint(10,240)
        g = random.randint(10,240)
        b = random.randint(10,240)
        cv2.circle(img,(x,y),15,(r,g,b),-1)
        mouseX,mouseY = x,y
    
h ,w ,c = img.shape
points = [(120, 110), (640-120, 110), (0, 430), (640, 430)]  # 150 # 100
pts1 = np.float32(points)

# find the width and height of the perspective transform image

pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])

# find the perspective transform matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# apply warpPerspective to get the perspective transform image
imgWarp = cv2.warpPerspective(img.copy(), matrix, (w, h))

coordinates = []


while True:
    # 
    cv2.imshow("img", img)
    cv2.setMouseCallback('img',draw_circle)
    # remove (0,0) from the list
    if (0,0) in coordinates:
        coordinates.remove((0,0))
    # coordinates.append((mouseX,mouseY))
    #  add (mouseX,mouseY) to the start of the list
    coordinates.insert(0,(mouseX,mouseY))
    
    # # remove duplicates from the list
    coordinates = list(set(coordinates))
        
    print(coordinates)
    # remove (0,0) from set
    
    cv2.imshow("imgWarp", imgWarp )
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        sys.exit()
