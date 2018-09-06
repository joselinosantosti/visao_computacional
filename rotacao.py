import cv2
img = cv2.imread('img/lena.jpg')
(alt, lar) = img.shape[:2] #captura altura e largura
centro = (lar // 2, alt // 2) #acha o centro
M = cv2.getRotationMatrix2D(centro, 30, 1.0) #30 graus
img_rotacionada = cv2.warpAffine(img, M, (lar, alt))
cv2.imshow("Imagem rotacionada em 45 graus", img_rotacionada)
cv2.waitKey(0)
