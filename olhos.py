#detecta os olhos

import numpy as np
import cv2

eye_cascade = cv2.CascadeClassifier('xml/haarcascade_eye.xml')

img = cv2.imread('img/lena.jpg')
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rostos = eye_cascade.detectMultiScale(cinza, 1.3, 5)
for (x,y,w,h) in rostos:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	roi_gray = cinza[y:y+h, x:x+w]
	roi_color = img[y:y+h, x:x+w]

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
