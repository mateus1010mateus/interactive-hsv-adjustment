#Deus é fiel Jesus toda honra e toda glória

import cv2
import numpy as np

# Variáveis globais para HSV e tolerância
hsv = [0, 0, 0]
tolerancia = [0, 0, 0]

# Função para calcular a tolerância média
def calcular_tolerancia_media(tolerancia):
    return int(sum(tolerancia) / len(tolerancia))

# Função para atualizar a imagem com os valores de HSV e tolerância
def atualizar_imagem():
    lower_bound = np.array([hsv[0] - tolerancia[0], hsv[1] - tolerancia[1], hsv[2] - tolerancia[2]])
    upper_bound = np.array([hsv[0] + tolerancia[0], hsv[1] + tolerancia[1], hsv[2] + tolerancia[2]])
    mask = cv2.inRange(imagem_hsv, lower_bound, upper_bound)
    resultado = cv2.bitwise_and(imagem, imagem, mask=mask)
    cv2.imshow('Imagem Atualizada', resultado)

# Função de callback para ajustar os valores de HSV e tolerância
def ajustar_valor(valor, indice):
    if indice < 3:
        hsv[indice] = valor
    else:
        tolerancia[indice - 3] = valor
    atualizar_imagem()

# Carregar a imagem
imagem = cv2.imread(r'C:\Users\Administrator\Documents\multiversus_bot\Screenshot_2.jpg')
imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Criar janela para a imagem
cv2.namedWindow('Imagem Atualizada')

# Definir os valores iniciais de HSV e tolerância
inicial_hsv = [0, 0, 0]
inicial_tolerancia = [0, 0, 0]

# Criar trackbars para ajustar os valores
for i in range(6):
    if i < 3:
        cv2.createTrackbar(chr(97 + i), 'Imagem Atualizada', inicial_hsv[i], 255, lambda x, i=i: ajustar_valor(x, i))
    else:
        cv2.createTrackbar(chr(97 + i), 'Imagem Atualizada', inicial_tolerancia[i - 3], 255, lambda x, i=i: ajustar_valor(x, i))

# Loop para ajustar os valores até encontrar a combinação desejada
while True:
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

# Calcular a tolerância média
tolerancia_media = calcular_tolerancia_media(tolerancia)

# Mostrar os valores de HSV e tolerância quando a tecla 's' for pressionada
print("HSV:", hsv)
print("Tolerância Média:", tolerancia_media)

# Fechar janelas
cv2.destroyAllWindows()
