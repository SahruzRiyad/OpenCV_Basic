import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./Image/lena_copy.png',1)
cv2.imshow('Image',img)

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.show()
plt.xticks([]),plt.yticks([])

cv2.waitKey(0)
cv2.destroyAllWindows()