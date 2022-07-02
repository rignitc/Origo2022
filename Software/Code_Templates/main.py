'''
# Author List:      RIG-NITC
# Theme:            Self Driving Car
# Filename:         main.py
# Functions:        generate_pwm
# Global variables: pwmR, pwmL, counter , midPoint, basePoint , Kp ,
#                   ip_cam_url, base, serverAddressPort, UDPClientSocket
                    imageTrackCenter, curveCenter
'''


####################### IMPORT MODULES #######################

import cv2
import numpy as np
import socket
import lane_detection as lane_detection
from traffic_sign_detection import sign_detection

##############################################################



msgFromClient = "124,120"
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("<Enter IP Address from NodeMCU>", 4210)  # get from the serial monitor
# bufferSize = 255
move_forward = False

# Create a UDP socket at client side
UDPClientSocket = socket.socket(
    family=socket.AF_INET, type=socket.SOCK_DGRAM)

ip_cam_url = "http://00.00.00.00:8080/video"  # IP Camera URL


averageCurveList = []

pwmR = 255  # constant pwm for right wheel #53
pwmL = 255  # contant pwm for left wheel

Kp = 0.5  # proportional gain #0.80
Kd = 0.25  # 0.2
prev_diff = 0

# Starting a video capture from the ip web cam
capture = cv2.VideoCapture(ip_cam_url)


def generate_pwm(diff):
    '''
    Purpose:
    ---
    Generate pwm for the wheels of the car based on the
    center of the track and the midpoint of the track
    Input Arguments:
    ---
    `imageTrackCenter` :  [ integer ]
            Average center of the track of in the image
    `curveCenter` :  [ integer ]
            Center of the lane considered near the bottom of the image

    Returns:
    ---
    None
    Example call:
    ---
    generate_pwm(300,240)
    '''
    global pwmR, pwmL, prev_diff
    
    ###### Write your control logic here ####


    ###### Control logic ends here #######

    if (pwmL < 100):
        pwmL = "0" + str(round(pwmL))
    else:
        pwmL = str(round(pwmL))
    if (pwmR < 100):
        pwmR = "0" + str(round(pwmR))
    else:
        pwmR = str(round(pwmR))

    

    bytesToSend = str.encode(pwmL + "," + pwmR)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    pwmR = 255
    pwmL = 255


def main():
    '''
    Purpose:
    ---
    Main function for the program
    Input Arguments:
    ---
    None
    Returns:
    ---
    None
    Example call:
    ---
    main()
    '''
    global pwmR, pwmL
    # global curveCenter, imageTrackCenter
    global move_forward, sign_detected

    while capture.isOpened():
        ret, img = capture.read()
        # cv2.imwrite("image.png",img)

        if ret:

            imgCopy = img.copy()

            img, sign_detected = sign_detection(img)
            if sign_detected == "stop":
                move_forward = False

            elif sign_detected == "start":
                move_forward = True

            if move_forward:

                #############   STEP 1  ##################  

                # apply thresholding to segment the track

                #### Code starts here ####

                #### Code ends here ####
                
                # cv2.imshow("original_img", img )
                cv2.imshow("thresholded", thresholded)


                ############# STEP 2  #####################

                # find the points to apply the perspective transform

                #### Code starts here ####

                #### Code ends here ####

                cv2.imshow("imgWarp", imgWarp )
                ``


                ############# STEP 3  #####################

                # get the track center and the lane center
                
                curveCenter, imgHist1 = lane_detection.getHistogram(
                    imgWarp, display=True, minPer=0.8)
                imageTrackCenter, imgHist2 = lane_detection.getHistogram(
                    imgWarp, display=True, minPer=0, region=4)    

                diff = imageTrackCenter - curveCenter
                 

                cv2.imshow("imgHist1", imgHist1)
                cv2.imshow("imgHist2", imgHist2)

                generate_pwm(diff)

            else:
                pwmR = 0
                pwmL = 0
                bytesToSend = str.encode("0"+str(pwmL) + "," + str(pwmR)+"0")
                # send the pwm values to the node mcu
                UDPClientSocket.sendto(bytesToSend, serverAddressPort)

            cv2.imshow('Original_image', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            capture.release()
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    main()