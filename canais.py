import cv2

#Abre a imagem filtrando canais
img= cv2.imread('img/lena.jpg')
cv2.imshow("Original", img)

#Cinza
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Cinza", cinza)

#3 canais
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b*", lab)
cv2.waitKey(0)
