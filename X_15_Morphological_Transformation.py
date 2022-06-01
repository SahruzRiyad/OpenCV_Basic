import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./Image/smarties.png',0)
_,mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
kernal = np.ones((2,2),np.uint8)
dilation = cv2.dilate(mask,kernal,iterations=2)
erosion = cv2.erode(mask,kernal,iterations=4) 
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
titles = ['Image' , 'Threshold' , 'Dilation','Erosion','Opening']
images = [img , mask , dilation , erosion , opening]

for  i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()