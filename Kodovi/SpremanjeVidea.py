import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'DIVX')
out = cv.VideoWriter('output.mp4', fourcc, 20000.0, (640,  480))
while True:
    ret, frame = cap.read()
    cv.imshow('frame', frame)
    out.write(frame)
    if cv.waitKey(25) and 0xff == ord('x'):
        break
    if cv.getWindowProperty('frame', cv.WND_PROP_VISIBLE) < 1:
        break

cap.release()
out.release() 
cv.destroyAllWindows()
