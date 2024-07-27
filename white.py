
import cv2
import numpy as np

cap=cv2.VideoCapture(1)

while True:
    _,frame=cap.read()
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    low=np.array([0,42,0])
    high=np.array([179,255,255])
    
    mask =cv2.inRange(hsv_frame, low, high)
    result =cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow('Frame',frame)
    cv2.imshow('Result',result)
    
    key=cv2.waitKey(1)
    if key==27:
        break
cap.release()
cv2.destroyAllWindows()
    
"""
import cv2
import numpy as np

cap = cv2.VideoCapture(1)  # Use 0 if you're using the default camera, 1 for an external camera

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    
    mask = cv2.inRange(hsv_frame, low, high)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow('Frame', frame)
    cv2.imshow('Result', result)
    
    key = cv2.waitKey(1)
    if key == 27:  # ESC key to break
        break

cap.release()
cv2.destroyAllWindows()
"""