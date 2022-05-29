import cv2

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

cap.set(cv2.CAP_PROP_FRAME_WIDTH,500)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,300)

print(cap.get(3)," ",cap.get(4))

while(cap.isOpened()):
    ret,frame = cap.read()
    cv2.imshow('Image',frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()