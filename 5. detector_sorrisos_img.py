import cv2
import numpy as np

sorrisos_detetor = cv2.CascadeClassifier('xml/haarcascade_smile.xml')

#while(True):
img = cv2.imread('img/sorriso.jpg')
	
img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sorrisos = sorrisos_detetor.detectMultiScale(img_cinza, 1.7, 33)
#sorrisos = detectorSorriso.detectMultiScale(img_cinza, scaleFactor= 1.7,minNeighbors=22,minSize=(25, 25),flags=cv2.cv.CV_HAAR_SCALE_IMAGE)

for (x, y, w, h) in sorrisos:
	cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,255), 2)

cv2.imshow('Sorrisos', img)
cv2.waitKey(0)

cv2.DestroyAllWindows()