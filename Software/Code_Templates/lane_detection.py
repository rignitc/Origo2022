import numpy as np
import cv2

def thresholding(img):
    '''
    Purpose:
    ---
    Thresholding the image to get the black track
    
    Input Arguments:
    ---
    `img` :  [ array ]
        The image to be thresholded
    Returns:
    `mask` : [ array ]
        The thresholded mask image
    ---
    Example call:
    ---
    mask = thresholding(img)
    '''
    
    imgHsv = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2HSV) # convert the image to hsv
    lowerWhite = np.array([0, 0, 0]) # create a lower range array
    upperWhite = np.array([179, 87, 255]) # create a upper range array
    maskWhite = cv2.inRange(img.copy(), lowerWhite, upperWhite) # create a mask for the image
    
    return maskWhite 

def getHistogram(img, minPer=0.5, display=False, region=1):
    '''
    Purpose:
    ---
    Get the histogram of the image
    
    Input Arguments:
    ---
    `img` : [ array ]
        The image to get the histogram of
    `minPer` : [ float ]
        The minimum percentage of the white region to be considered to be the white track
        eg : 255 is considered as perfect track and 0 is not considered as track
            if minPer = 0.8 then 255*0.8 = 204 
            all the regions with value less than 204 will not be considered as track
    `display` : [ bool ]
        Whether or not to visualize the histogram of the image
    `region` : [ int ]
        The region of the image to be considered for the histogram calculation
    Returns:
    `averageCurveValue` : [ integer ]
        The average value of the track center
    `histogram` : [ array ]
        The histogram of the image
    ---
    Example call:
    ---
    imageTrackCenter, histogram = getHistogram(img , minPer=0.5, display=True, region=1)
    laneCenter = getHistogram(img , minPer=0.8, display=False, region=4)
    '''

    
    if region == 1:
        # find the coloumn sum of entire pixels in the image
        histValues = np.sum(img, axis=0) # sum the pixels in the image
    else:
        histValues = np.sum(img[img.shape[0] // region:, :], axis=0) # sum the pixels of specific region in the image
    #
    # print(histValues)
    maxValue = np.max(histValues)
    minValue = minPer * maxValue
    
    # imageTrackCenter ,laneCenter
    indexArray = np.where(histValues >= minValue)
    laneCenter = int(np.average(indexArray))
    
    # print(histValues)

    if display:
        imgHist = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
        for x, intensity in enumerate(histValues):
            print(f"line between {x, img.shape[0]} and {x,np.int(img.shape[0] - intensity // 255 // region)}")
            cv2.line(imgHist, (x, img.shape[0]), (x, np.int(img.shape[0] - intensity // 255 // region)), (255, 0, 255),1)
            cv2.circle(imgHist, (laneCenter, img.shape[0]), 20, (0, 255, 255), cv2.FILLED)
        return laneCenter, imgHist

    return laneCenter


img = cv2.imread('location to lane.jpg')
w, h = img.shape[:2]

img_threshold = thresholding(img)


points = np.float32([(190, 150), (440, 150), (0, 460), (640, 460)]) # create a list of points
pts1 = np.float32(points)

pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]]) # points to be mapped
matrix = cv2.getPerspectiveTransform(pts1, pts2) # get the transformation matrix
imgWarp = cv2.warpPerspective(img_threshold, matrix, (w, h)) # warp the image

imageTrackCenter, imgHist_1 = getHistogram(imgWarp, display=True, minPer=0.8, region=3)
laneCenter, imgHist_2 = getHistogram(imgWarp, display=True, minPer=0.8)


cv2.imshow('image', img)
cv2.imshow('image_threshold', img_threshold)
cv2.imshow('image_warp', imgWarp)
cv2.imshow('image_hist_1', imgHist_1)
cv2.imshow('image_hist_2', imgHist_2)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()