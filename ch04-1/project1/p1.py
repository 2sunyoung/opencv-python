import numpy as np
import cv2
cntM=0
cntLU=0
cntLD=0
def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global cntLD
        cntLD+=1
        print(f"EVENT_LBUTTONDOWN: {cntLD}")
    elif event == cv2.EVENT_LBUTTONUP:
        global cntLU
        cntLU+=1
        print(f"EVENT_LBUTTONUP, {cntLU}")
    elif event == cv2.EVENT_MOUSEMOVE:
        global cntM
        cntM+=1
        print(f"EVENT_MOUSEMOVE, {cntM}")
image = cv2.imread('lenna.bmp')
cv2.imshow('Mouse Event', image)
cv2.setMouseCallback('Mouse Event', onMouse)

while True:
    key = cv2.waitKey(1) 
    if key == 27: break
cv2.destroyAllWindows() 
