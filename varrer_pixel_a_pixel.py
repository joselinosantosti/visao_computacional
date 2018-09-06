import cv2
imagem = cv2.imread('img/lena.jpg')
for y in range(0, imagem.shape[0]):
	#print(y)
	for x in range(0, imagem.shape[1]):
		#print(x)
		imagem[y, x] = (255,0,0) #tudo azul
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)
cv2.imwrite("azul.jpg", imagem)
