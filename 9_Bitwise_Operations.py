import cv2
import numpy as np

img1 = cv2.imread('LinuxLogo.jpg')
img2 = np.zeros((240,320,3),np.uint8)
img2 = cv2.rectangle(img2,(0,0),(230,320),(255,255,255),-1)

#bitAnd = cv2.bitwise_and(img2,img1)
#bitOr = cv2.bitwise_or(img2,img1)
#bitXor = cv2.bitwise_xor(img2,img1)
bitNot = cv2.bitwise_not(img1)

cv2.imshow('Image2',img2)
cv2.imshow('Image1',img1)
cv2.imshow('Image3',bitNot)
cv2.waitKey(0)
cv2.destroyAllWindows()