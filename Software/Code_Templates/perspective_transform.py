import numpy as np
import cv2
import os
import sys


dir_path = os.path.dirname(os.path.realpath(__file__))
img = cv2.imread(dir_path+'/lane.jpg')

h ,w ,c = img.shape
points = [(120, 110), (640-120, 110), (0, 430), (640, 430)]  # 150 # 100
pts1 = np.float32(points)

# find the width and height of the perspective transform image

pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])

# find the perspective transform matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# apply warpPerspective to get the perspective transform image
imgWarp = cv2.warpPerspective(img.copy(), matrix, (w, h))

cv2.imshow("imgWarp", imgWarp )
cv2.imshow("img", img)
if cv2.waitKey(0) & 0xFF == ord('q'):
    sys.exit()
