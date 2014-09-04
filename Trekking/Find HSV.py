import cv2
import numpy as np

#Insert values of BGR Color below:
color = np.uint8([[[255, 0, 0]]])
hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
print hsv_color
print("Now you take [H-10, 100,100] and [H+10, 255, 255] as lower bound and upper bound respectively.")
