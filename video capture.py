"""
import cv2 
import numpy as np

#cap=cv2.VideoCapture('http://192.168.0.138:4747/video')
cap=cv2.VideoCapture(1)
while True:
    _,frame = cap.read()
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #red color mask
    low_red=np.array([161,155,84])
    high_red=np.array([179,255,255])
    
    red_mask=cv2.inRange(hsv_frame,low_red,high_red)
    
    red=cv2.bitwise_and(frame,frame,mask=red_mask)
    
    #blue color mask
    
    low_blue=np.array([15,80,2])
    high_blue=np.array([126,255,255])
    blue_mask=cv2.inRange(hsv_frame,low_blue,high_blue)
    blue=cv2.bitwise_and(frame,frame,mask=blue_mask)
    
    #Green color mask
    
    low_green =np.array([25,52,72])
    high_green = np.array([102,255,255])
    green_mask=cv2.inRange(hsv_frame,low_green,high_green)
    green=cv2.bitwise_and(frame,frame,mask=green_mask)
    
    
    
    cv2.imshow('Frame',frame)
    cv2.imshow('red',red)
    cv2.imshow('blue',blue)
    cv2.imshoww('green',green)
    
    key=cv2.waitKey(1)
    if key == 27:
        break
"""
import cv2
import numpy as np

#cap = cv2.VideoCapture('http://192.168.0.138:4747/video') # Use this if you're capturing from an IP camera
cap = cv2.VideoCapture(1) # Use 0 for the default camera, 1 for the first external camera

# Create resizable windows
cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
cv2.namedWindow('Red', cv2.WINDOW_NORMAL)
cv2.namedWindow('Blue', cv2.WINDOW_NORMAL)
cv2.namedWindow('Green', cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Red color mask
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    
    # Blue color mask
    #low_blue = np.array([15, 80, 2])
    #high_blue = np.array([126, 255, 255])
    low_blue = np.array([100, 150, 0])
    high_blue = np.array([140, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
    
    # Green color mask
    low_green = np.array([35, 52, 72])
    high_green = np.array([85, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    
    # Display the frames
    cv2.imshow('Frame', frame)
    cv2.imshow('Red', red)
    cv2.imshow('Blue', blue)
    cv2.imshow('Green', green)
    
    key = cv2.waitKey(1)
    if key == 27: # ESC key to break
        break

cap.release()
cv2.destroyAllWindows()


    
    
