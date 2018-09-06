import numpy as np
import cv2

imagem = cv2.imread('img/lena.jpg')
fonte = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagem,'Lena',(15,65), fonte,
2,(255,255,255),2,cv2.LINE_AA)
cv2.imshow("Lena", imagem)
cv2.waitKey(0)

