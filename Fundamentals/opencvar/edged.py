import cv2

img = cv2.imread(r'unnamed.png',0)
edges = cv2.Canny(img, 100, 200)

cv2.imshow("Edge Detected Image", edges)
cv2.imshow("Original Image", img)
cv2.waitkey(0)
cv2.destroyAllWindows()


