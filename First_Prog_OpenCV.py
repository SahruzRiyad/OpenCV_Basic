import cv2

path = './opencv-4.x/samples/data/'
img = cv2.imread(path+'lena.jpg',1)

print(img)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png',img)