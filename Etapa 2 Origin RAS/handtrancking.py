# Importação de bibliotecas
import cv2
import mediapipe as mp

# Variável quecaptura o video em tempo real da câmera
video = cv2.VideoCapture(0)

# Variável que usa as configurações
# da solução 'hands' da biblioteca mp
hand = mp.solutions.hands
# Variável que recebe como parâmetro
# o número máximo de mãos e faz
# a detecção da mão dentro do vídeo
Hand = hand.Hands(max_num_hands=1)
# Variável que desenha as ligações entre
# os pontos na mão
mdDraw = mp.solutions.drawing_utils

# Laço que faz uso da câmera
while True:
    # Variável que recebe o vídeo
    check,img = video.read()
    # Converte a imagem recebida de BGR para RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Variável que processa a imagem em RGB
    results = Hand.process(imgRGB)
    # Variável que extrai as coordenadas dos pontos da mão
    handsPoints = results.multi_hand_landmarks
    # Variáveis que contém as dimensões da imagem
    h,w,_= img.shape
    # array que recebe os valores por frame
    pontos = []
    # Condição para que não funcione com a variável
    # handsPoints vazia
    if handsPoints:
        # Laço que percorre os pontos da mão
        for points in handsPoints:
            # Desenha as conexões entre os pontos na mão
            mdDraw.draw_landmarks(img,points,hand.HAND_CONNECTIONS)
            # Laço que enumera cada ponto da mão
            for id,cord in enumerate(points.landmark):
                # Variáveis que convertem os landmarks em píxels
                cx,cy = int(cord.x*w), int(cord.y*h)
                # Incrementa os valores por frame na array
                pontos.append((cx,cy))
        # array que contém os pontos superiores de cada dedo
        dedos = [8,12,16,20]
        # variável que receberá qual número deve ser exibido
        contador = 0
        # Condições para contagem dos dedos
        if points:
            # Casos para o polegar fechado
            if pontos[4][0] > pontos[2][0]:
                # Todos os dedos fechados resulta no número 0
                if (pontos[8][1]>pontos[6][1])&(pontos[12][1]>pontos[10][1])&(pontos[16][1]>pontos[14][1])&(pontos[20][1]>pontos[18][1]):
                    contador=0
                # Apenas o indicador levantado resulta no número 1
                if (pontos[8][1]<pontos[6][1])&(pontos[12][1]>pontos[10][1])&(pontos[16][1]>pontos[14][1])&(pontos[20][1]>pontos[18][1]):
                    contador=1
                # Indicador e médio levantados resultado no número 2
                if (pontos[8][1]<pontos[6][1])&(pontos[12][1]<pontos[10][1])&(pontos[16][1]>pontos[14][1])&(pontos[20][1]>pontos[18][1]):
                    contador=2
                # Indicador, médio e anelar levantados resulta no número 3
                if (pontos[8][1]<pontos[6][1])&(pontos[12][1]<pontos[10][1])&(pontos[16][1]<pontos[14][1])&(pontos[20][1]>pontos[18][1]):
                    contador=3
                # Todos os dedos menos o polegar levantados resulta no número 4
                if (pontos[8][1]<pontos[6][1])&(pontos[12][1]<pontos[10][1])&(pontos[16][1]<pontos[14][1])&(pontos[20][1]<pontos[18][1]):
                    contador=4
                # Indicador e midinho levantados resulta no número 6
                if (pontos[8][1]<pontos[6][1])&(pontos[12][1]>pontos[10][1])&(pontos[16][1]>pontos[14][1])&(pontos[20][1]<pontos[18][1]):
                    contador=6
                # Indicador, anelar e midinho levantados resulta no número 7
                if (pontos[8][1]<pontos[6][1])&(pontos[12][1]>pontos[10][1])&(pontos[16][1]<pontos[14][1])&(pontos[20][1]<pontos[18][1]):
                    contador=7
                # Indicador, médio e midinho levantados resulta no número 8
                if (pontos[8][1]<pontos[6][1])&(pontos[12][1]<pontos[10][1])&(pontos[16][1]>pontos[14][1])&(pontos[20][1]<pontos[18][1]):
                    contador=8
                # Apenas o midinho levantado resulta no número 9
                if (pontos[8][1]>pontos[6][1])&(pontos[12][1]>pontos[10][1])&(pontos[16][1]>pontos[14][1])&(pontos[20][1]<pontos[18][1]):
                    contador=9
            # Casos para o polegar aberto
            if pontos[4][0] < pontos[2][0]:
                # Todos os dedos levantados resulta no número 5
                if (pontos[8][1]<pontos[6][1])&(pontos[12][1]<pontos[10][1])&(pontos[16][1]<pontos[14][1])&(pontos[20][1]<pontos[18][1]):
                    contador=5
                # Polegar e midinho levantados resulta no número 10
                if (pontos[8][1]>pontos[6][1])&(pontos[12][1]>pontos[10][1])&(pontos[16][1]>pontos[14][1])&(pontos[20][1]<pontos[18][1]):
                    contador=10
        # Criação de retangulo para exibição do contador na imagem
        cv2.rectangle(img,(80,10),(200,100),(0,255,0),-1)
        cv2.putText(img,str(contador),(100,100),cv2.FONT_HERSHEY_SIMPLEX,4,(0,0,255),5)
    # Exibição da imagem
    cv2.imshow("imagem", img)
    cv2.waitKey(1)
    