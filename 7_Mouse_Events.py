import cv2
from cv2 import EVENT_LBUTTONDOWN
import numpy as np

def click_event(event,x,y,flags,param):
    if event == EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(0,0,255),-1)
        points.append((x,y))
        if len(points) > 1:
            cv2.line(img,(x,y),(points[-2]),(255,255,255),3)
        cv2.imshow('Image',img)

img = np.zeros((512,512,3),np.uint8)
cv2.imshow('Image',img)
points = []
cv2.setMouseCallback('Image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()