import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)

while(cap.isOpened()):
    ret,frame = cap.read()
    hand,frame = detector.findHands(frame)
    cv2.imshow('Image',frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()