import cv2
import numpy as np

#insert HSV range
print('Define color range:')
low_color = tuple(input('HSVmin: '))
up_color = tuple(input('HSVmax: '))

#Start recording
cap = cv2.VideoCapture(0)

while(1):

    #Take each frame
    _, frame = cap.read()
    
    #Convert to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Threshold
    mask = cv2.inRange(hsv, low_color, up_color)

    #Bitwise_AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('Capture', frame)
    cv2.imshow('Result', res)

    if cv2.waitKey(30) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()
