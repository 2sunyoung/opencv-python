import cv2
import numpy as np

image = np.zeros((400, 1200, 3), np.uint8)

h, w = image.shape[:2]

w1 = w // 3    
w2 = 2 * w // 3  

z1 = image[0:h, 0:w1]   
z2 = image[0:h, w1:w2]    
z3 = image[0:h, w2:w]    

z1[:] = (255, 0, 0)   
z2[:] = (0, 255, 0)   
z3[:] = (0, 0, 255)   

white = (255, 255, 255)

cv2.line(z1, (100, 100), (300, 100), white, 15)
cv2.line(z1, (300, 100), (300, 300), white, 15)
cv2.line(z1, (300, 300), (100, 300), white, 15)
cv2.line(z1, (100, 300), (100, 100), white, 15)

cv2.circle(z2, (200, 200), 100, white, 15)

cv2.line(z3, (100, 100), (300, 300), white, 15)
cv2.line(z3, (300, 100), (100, 300), white, 15)

cv2.imshow('img', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
