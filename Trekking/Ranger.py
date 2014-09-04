import sys
import cv2
import numpy as np

#set image
filename = str(raw_input("Put image path: "))
img = cv2.imread(filename)

#error while reading image
if img is None:
   print "ERROR: file could not be opened!"
   exit()

#resizes and copy image
img = cv2.resize(img,(800,600))
copy = img.copy()
hsv_img = cv2.cvtColor(copy,cv2.COLOR_BGR2HSV)

#global variables for mouse callback function
count = ix = iy = 0
drawing = False
limits = ((-1,-1),(-1,-1))

def draw_square(event,x,y,flags,param):
   global ix,iy,drawing,limits,copy,img
   
   if event == cv2.EVENT_LBUTTONDOWN:
      drawing = True
      ix,iy = x,y

   elif event == cv2.EVENT_MOUSEMOVE:
      if drawing == True:
         img = copy.copy()
         cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),1)
         limits = ((ix,iy),(x,y))

   elif event == cv2.EVENT_LBUTTONUP:
      drawing = False   

def medianPixel(img):
   summ = 0
   median = [0,0,0]
   for i in range(img.shape[0]):
      for j in range(img.shape[1]):
         array = img[i,j]
         for k in range(len(array)):
            median[k] += array[k]
         summ += 1
   median = tuple(i/summ for i in median)
   return median 

#bind the function to window
winame = "image"
cv2.namedWindow(winame)
cv2.setMouseCallback(winame,draw_square)

#function loop
while(True):
    cv2.imshow(winame,img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

ix,iy = limits[0]
x,y   = limits[1]

if (ix > x):
   limits = ((x,limits[0][1]),(ix,limits[1][1]))
if (iy > y):
   limits = ((limits[0][0],y),(limits[1][0],iy))


#creates specific image
lim_img = img[limits[0][1]:limits[1][1],limits[0][0]:limits[1][0]]
hsv_lim_img = cv2.cvtColor(lim_img,cv2.COLOR_BGR2HSV)

#creates red rectangle on image
cv2.rectangle(img,limits[0],limits[1],(0,0,255),1)
cv2.imshow(winame,img)
cv2.waitKey(0)
img = copy.copy()

#hue and saturation values
min_hue = min_sat = min_val = 0
max_hue = 180
max_sat = max_val = 255

#calculating median
median = medianPixel(hsv_lim_img)
hsv_ft = (int(max_hue*0.05),int(max_sat*0.08),int(max_val*0.1))
hsv_min = (int(median[0]-hsv_ft[0]),int(median[1]-hsv_ft[1]),int(median[2]-hsv_ft[2]))
hsv_max = (int(median[0]+hsv_ft[0]),int(median[1]+hsv_ft[1]),int(median[2]+hsv_ft[2]))

print "median,hsv_ft =",median,hsv_ft
print "hsv_min,hsv_max =",hsv_min,hsv_max

#thresholding
threshed = cv2.inRange(hsv_img,hsv_min,hsv_max)
cv2.imshow(winame,threshed)
cv2.waitKey(0)

cv2.destroyAllWindows()
