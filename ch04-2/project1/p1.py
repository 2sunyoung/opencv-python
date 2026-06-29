import cv2
import numpy as np

image = np.zeros((400, 400, 3), np.uint8)
image.fill(255)

h, w = image.shape[:2] 

pt1 = (w//4, h//4)
pt2 = (3*w//4, h//4)
pt3 = (3*w//4, 3*h//4)
pt4 = (w//4, 3*h//4)

cv2.line(image, pt1, pt2, 0)
cv2.line(image, pt2, pt3, 0)
cv2.line(image, pt3, pt4, 0)
cv2.line(image, pt4, pt1, 0)
cv2.line(image, pt1, pt3, 0)
cv2.line(image, pt2, pt4, 0)

cv2.imshow("src", image)
cv2.waitKey(0)

image.fill(255)

cv2.line(image, pt1, pt2, 0)
cv2.line(image, pt2, pt3, 0)
cv2.line(image, pt3, pt4, 0)
cv2.line(image, pt4, pt1, 0)

cv2.circle(image, (w//2, h//2), w//4, 0, 1)

cv2.imshow("src", image)
cv2.waitKey(0)

cv2.destroyAllWindows()
