#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Importação das bibliotecas
import cv2

# Leitura da imagem com a função imread()
imagem = cv2.imread('img/estrada.jpg')
print('Largura em pixels: ')
print(imagem.shape[1]) #largura da imagem
print('Altura em pixels: ')
print(imagem.shape[0]) #altura da imagem
print('Qtde de canais: ')
print(imagem.shape[2])

print "Altura (height): %d pixels" % (imagem.shape[0])
print "Largura (width): %d pixels" % (imagem.shape[1])
print "Canais (channels): %d"      % (imagem.shape[2])

cv2.imshow("Nome da janela", imagem) # Mostra a imagem com a função imshow
cv2.waitKey(0) #espera pressionar qualquer tecla
cv2.imwrite("saida.jpg", imagem) # Salvar a imagem no disco com função imwrite() dando um nome para ela
