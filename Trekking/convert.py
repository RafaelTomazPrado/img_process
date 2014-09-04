import cv2

cv2.namedWindow("Grayscale", cv2.WINDOW_AUTOSIZE)
img = cv2.imread("C:\Users\Rafael\Pictures\Sape_Logo.png")
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", img2)
cv2.waitKey()
cv2.destroyAllWindows
