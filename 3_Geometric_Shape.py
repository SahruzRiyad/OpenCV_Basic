import numpy as np
import cv2
from cv2 import imread
path = './opencv-4.x/samples/data/'

img = imread(path+'lena.jpg',1)
#img = np.zeros([512,512,3],np.uint8)

#BGR format(0,0,255)-> for Red
img = cv2.line(img,(0,0),(255,255),(147,96,44),10)
img = cv2.arrowedLine(img,(0,255),(255,255),(0,255,0),10)
img = cv2.rectangle(img,(384,0),(510,128),(0,0,255),4)
img = cv2.circle(img,(447,63),63,(0,255,0),-1)

fontFace = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img,"OpenCv Basic",(10,500),fontFace,4,(255,255,255),10,cv2.LINE_AA)
cv2.imshow('Image',img)
cv2.waitKey(5000)
cv2.destroyAllWindows()