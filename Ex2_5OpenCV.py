#importação de bibliotecas
import cv2

# leitura da imagem
imagem = cv2.imread('entrada.jpg')

#laço que percorre a imagem e coloca agrupamentos de 5x5 pixels na cor amarelo a cada 10 pixels percorridos nas linhas e colunas
for y in range(0, imagem.shape[0], 10):
    for x in range(0, imagem.shape[1], 10):
        imagem[y:y+5,x:x+5] = (0, 255, 255)

#mostra a imagem modificada
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0) # espera pressionar qualquer tecla
