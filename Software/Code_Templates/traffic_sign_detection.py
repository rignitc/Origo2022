'''
# Author List:      RIG-NITC
# Theme:            Self Driving Car
# Filename:         traffic_sign_detection.py
# Functions:        sign_detection
# Global variables: None
'''

import cv2
import os
# get current file path
dir_path = os.path.dirname(os.path.realpath(__file__))


left = cv2.CascadeClassifier(dir_path+'/sign_left.xml')
right= cv2.CascadeClassifier(dir_path+'/sign_right.xml')
stop = cv2.CascadeClassifier(dir_path+'/sign_stop.xml')
start= cv2.CascadeClassifier(dir_path+'/sign_start.xml')


def sign_detection(img):
    '''
    Purpose:
    ---
    Detects traffic signs in an image.

    Input Parameters:
    ---
    img: image to be processed

    Return Values:
    ---
    img: image with traffic signs detected
    sign_detected: string indicating the type of traffic sign detected
    '''

    # convert to grayscale
    sign_detected = ""

    # convert to grayscale
    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detect stop sign

    S1 = stop.detectMultiScale(gray, 1.3,5) # stop
    S2 = start.detectMultiScale(gray, 1.521,8) # start
    S3 = right.detectMultiScale(gray, 1.161,8) # right
    S4 = left.detectMultiScale(gray, 1.207,4) # left

    # draw a rectangle around the stop sign
    for x,y,w,h in S1 :           
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(250,0,0),2)
        img = cv2.putText(img, 'stop', (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,50,50), 2, cv2.LINE_AA)
        sign_detected="stop"

    # draw a rectangle around the start sign
    for x,y,w,h in S2 :           
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(250,0,0),2)
        img = cv2.putText(img, 'start', (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,50,50), 2, cv2.LINE_AA)
        sign_detected="start"    

    # draw a rectangle around the right sign
    for x,y,w,h in S3 :
        area = w*h
        minArea = 0
        if area  > minArea:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(250,0,0),2)
            img = cv2.putText(img, 'right', (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,50,50), 2, cv2.LINE_AA) 
            sign_detected="right"  
        
    # draw a rectangle around the left sign 
    for x,y,w,h in S4 :
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(250,0,0),2)
        img = cv2.putText(img, 'left', (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,50,50), 2, cv2.LINE_AA)
        sign_detected="left"

    return img,sign_detected    