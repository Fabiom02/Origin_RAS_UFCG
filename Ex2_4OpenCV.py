#importação de bibliotecas
import cv2

# leitura da imagem
imagem = cv2.imread('entrada.jpg')

#laço que percorre a imagem e coloca os pixels como linhas verdes
for y in range(0, imagem.shape[0], 1):
    for x in range(0, imagem.shape[1], 1):
        imagem[y,x] = (0, (x*y)%256, 0)

#mostra a imagem modificada
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0) # espera pressionar qualquer tecla
