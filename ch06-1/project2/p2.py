import numpy as np
import cv2

def onChange(value):
    bright = cv2.add(image, value)
    cv2.imshow("dst", bright)

image = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("파일 읽기 오류")

cv2.imshow("dst", image)
cv2.createTrackbar("Brightness", "dst", 0, 100, onChange)

while True:
    if cv2.waitKey(1000) == 27: break
cv2.destroyAllWindows()
