#importação de bibliotecas
import cv2

# leitura da imagem
imagem = cv2.imread('entrada.jpg')

#laço que percorre a imagem e coloca os pixels como componentes de cor entre valores de 0 a 255
for y in range(0, imagem.shape[0]):
    for x in range(0, imagem.shape[1]):
        imagem[y,x] = (x%256, y%256, x%256)

#mostra a imagem modificada
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0) # espera pressionar qualquer tecla
