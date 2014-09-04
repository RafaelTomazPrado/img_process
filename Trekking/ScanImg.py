import cv2
import numpy as np

#load image
filename = str(raw_input("Image path: "))

#read image
img = cv2.imread(filename)

#resize
img = cv2.resize(img, (800,600))

#convert to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#set range
print("Digite os valores no formato: H,S,V")
hsv_min = tuple(input("Min: "))
hsv_max = tuple(input("Max: "))

#Color range
lower_color = np.array([hsv_min])
upper_color = np.array([hsv_max])

#Threshold
mask = cv2.inRange(hsv, lower_color, upper_color)

#bitwise_AND mask and original file
res = cv2.bitwise_and(img, img, mask = mask)

cv2.imshow('Image', img)
cv2.imshow('Result', res)

while True:
    k = cv2.waitKey(0) & 0xFF
    if k == 27: break
    
cv2.destroyAllWindows()
