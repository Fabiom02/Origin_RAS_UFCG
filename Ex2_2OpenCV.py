#importação de bibliotecas
import cv2

# leitura da imagem
imagem = cv2.imread('entrada.jpg')

#laço que troca faz os pixels da imagem ficarem azuis
for y in range(0, imagem.shape[0]):
    for x in range(0, imagem.shape[1]):
        imagem[y,x] = (255,0,0)

#mostra a imagem modificada
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0) # espera pressionar qualquer tecla
