import cv2
imagem = cv2.imread('img/lena.jpg')
				#linhas   colunas
recorte = imagem[100:200, 100:200]
cv2.imshow("Recorte da imagem", recorte)
cv2.imwrite("recorte.jpg", recorte) #salva no disco
