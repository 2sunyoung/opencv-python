import cv2
import numpy as np

img = np.zeros((300, 300,3), np.uint8)

cnt = 0   
a = False 

while True:
    img[:] = 255
    
    cv2.putText(img, str(cnt), (110, 180), cv2.FONT_HERSHEY_SIMPLEX,3, (0, 0,0), 5)
    cv2.imshow('img', img)
    
    if a == True:
        key = cv2.waitKey(1000)
        cnt += 1  
    else:
        key = cv2.waitKey(0)
        
    if key == ord('s'):
        a = True
    elif key == ord('t'): 
        a = False
    elif key == ord('r'):   
        cnt = 0
    elif key == ord('q'):  
        break

cv2.destroyAllWindows()
