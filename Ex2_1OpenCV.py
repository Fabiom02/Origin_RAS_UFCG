# importação das bibliotecas
import cv2

# leitura da imagem
imagem = cv2.imread('entrada.jpg')
(b, g, r) = imagem[0,0] # retorna os valores das cores do pixel superior mais a esquerda
print('O pixel (0,0) tem as seguintes cores: ')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b )