import cv2
import numpy as np

events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,",",y)
        font = cv2.FONT_HERSHEY_COMPLEX
        text = str(x) + ","+str(y)
        cv2.putText(img,text,(x,y),font,1,(0,0,255),3)
        cv2.imshow('Image',img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_COMPLEX
        text = str(blue) + ","+str(green)+","+str(red)
        cv2.putText(img,text,(x,y),font,1,(0,255,255),2)
        cv2.imshow('Image',img)


img = cv2.imread('lena_copy.png')
cv2.imshow('Image',img)
cv2.setMouseCallback('Image',click_event)
cv2.waitKey(0)#Press Esc to quit
cv2.destroyAllWindows()