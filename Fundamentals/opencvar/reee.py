#grey scale
import cv2
img=cv2.imread(r'C:\Users\USER\PycharmProjects\pythonProject\Fundamentals\opencvar\unnamed.png',0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()