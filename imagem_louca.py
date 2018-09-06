import cv2
imagem = cv2.imread('img/lena.jpg')
for y in range(0, imagem.shape[0], 1): #percorre as linhas
	for x in range(0, imagem.shape[1], 1): #percorre as colunas
		#imagem[y, x] = (0,(x*y)%256,0)
		imagem[y, x] = (0,x*y,y*x)
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)