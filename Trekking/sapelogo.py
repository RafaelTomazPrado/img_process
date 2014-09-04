import cv2
import numpy as np

#read image
img = cv2.imread("C:\Users\Rafael\Pictures\Sape_Logo.png")

#convert to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#Set range
lower_orange = np.array([10,235,219])
upper_orange = np.array([28,275,269])

#Threshold
mask = cv2.inRange(hsv, l_color, u_color)

#bitwise_AND maks and original file
res = cv2.bitwise_and(img, img, mask = mask)

cv2.imshow('Image', img)
cv2.imshow('Mask', mask)
cv2.imshow('Result', res)
k = cv2.waitKey(5) & 0xFF == 27


cv2.destroyAllWindows
