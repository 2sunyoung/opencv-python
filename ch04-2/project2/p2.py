import cv2
import numpy as np

image = cv2.imread('lenna.bmp')

if image is None:
    raise Exception("'lenna.bmp' 파일을 불러올 수 없습니다")

h, w = image.shape[:2] 

x1 = w // 4
x2 = w // 2
x3 = 3 * w // 4

y1 = h // 4
y2 = h // 2
y3 = 3 * h // 4

white = (255, 255, 255)

cv2.line(image, (x1, 0), (x1, h), white)
cv2.line(image, (x2, 0), (x2, h), white)
cv2.line(image, (x3, 0), (x3, h), white)

cv2.line(image, (0, y1), (w, y1), white)
cv2.line(image, (0, y2), (w, y2), white)
cv2.line(image, (0, y3), (w, y3), white)

cv2.line(image, (0, 0), (w, 0), white)    
cv2.line(image, (0, 0), (0, h), white)   
cv2.line(image, (0, h-1), (w, h-1), white)   

cv2.imshow('Line', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
