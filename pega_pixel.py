#identifica a cor do pixel escolhido
import cv2
imagem = cv2.imread('img/estrada.jpg')
(b, g, r) = imagem[0, 0] #veja que a ordem BGR e nao RGB

print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

