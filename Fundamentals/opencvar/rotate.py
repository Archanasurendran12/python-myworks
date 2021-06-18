#image rotation
import cv2
#read image as greyscale
img=cv2.imread(r'C:\Users\USER\PycharmProjects\pythonProject\Fundamentals\opencvar\unnamed.png',0)
#get imge hight and width
(h,w)=img.shape[:2]
#calculate the center of the image
center=(w/2,h/2)
angle90=90
angle180=180
angle270=270
scale=1.0
#prform the counterclockwis rotation holding at the cntr
#90 degrees
M=cv2.getRotationMatrix2D(center,angle90,scale)
rotated90=cv2.warpAffine(img,M,(h,w))
#180 degrees
M=cv2.getRotationMatrix2D(center,angle180,scale)
rotated180=cv2.warpAffine(img,M,(h,w))
#270 degrees
M=cv2.getRotationMatrix2D(center,angle270,scale)
rotated270=cv2.warpAffine(img,M,(h,w))
cv2.imshow('original image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('image rtated by 90 degrees',rotated90)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('image rtated by 180 degrees',rotated180)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('image rtated by 270 degrees',rotated270)
cv2.waitKey(0)
cv2.destroyAllWindows()