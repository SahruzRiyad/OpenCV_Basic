import cv2
from cv2 import bitwise_and
import numpy as np

def nothing(x):
    print(x)

cap = cv2.VideoCapture(0)

cv2.namedWindow('Tracking')
cv2.createTrackbar('LH','Tracking',0,255,nothing)
cv2.createTrackbar('LS','Tracking',0,255,nothing)
cv2.createTrackbar('LV','Tracking',0,255,nothing)
cv2.createTrackbar('HH','Tracking',255,255,nothing)
cv2.createTrackbar('HS','Tracking',255,255,nothing)
cv2.createTrackbar('HV','Tracking',255,255,nothing)


while True:
    #frame = cv2.imread('smarties.png')
    ret,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos('LH','Tracking')
    l_s = cv2.getTrackbarPos('LS','Tracking')
    l_v = cv2.getTrackbarPos('LV','Tracking')
   
    u_h = cv2.getTrackbarPos('HH','Tracking')
    u_s = cv2.getTrackbarPos('HS','Tracking')
    u_v = cv2.getTrackbarPos('HV','Tracking')

    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv,l_b,u_b)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow('Mask',mask)
    cv2.imshow('Res',res)
    cv2.imshow('Image',frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()