import cv2

#Carrega arquivo e converte para tons de cinza
imagem = cv2.imread('img/lena.jpg')
img_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

#Criacao do detector de faces com a tecnica haar_cascade
detector = cv2.CascadeClassifier('xml/frontalface.xml')

#Executa a detector (pulo do gato)
faces = detector.detectMultiScale(img_cinza, scaleFactor = 1.05, minNeighbors = 7, minSize = (30,30), flags = cv2.CASCADE_SCALE_IMAGE)

#Desenha retangulos azuis na imagem original (colorida)
for (x, y, w, h) in faces:
	cv2.rectangle(imagem, (x, y), (x + w, y + h), (255, 0, 0), 7)

#Exibe imagem. Titulo da janela e numero de faces
cv2.imshow(str(len(faces))+' face(s) encontrada(s).', imagem)
cv2.waitKey(0)
