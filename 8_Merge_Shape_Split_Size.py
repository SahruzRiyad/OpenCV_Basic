import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')
print(img.shape)
print(img.size)
print(img.dtype)

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

#ROI= Region of Interest
#cv2.rectangle(img,(333,285),(390,337),(0,255,0),0)
ball = img[285:337,333:390]
#cv2.imwrite('ball.png',ball)
img[273:325,100:157] = ball
#print(ball.shape)

img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))

dst = cv2.add(img,img2)#Merge two image (src1 , src2)
dst1 = cv2.addWeighted(img,.7,img2,.3,0)#Add weight to image (src1,alpha,src2,beta,gamma)
cv2.imshow('Image',dst1)
cv2.waitKey(0)
cv2.destroyAllWindows()
