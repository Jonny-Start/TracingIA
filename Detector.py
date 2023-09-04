import cv2
from Rastreador import *

# Crear objeto de seguimiento
seguimiento = Rastreador()

# Lectura del video
#cap = cv2.VideoCapture("prueba.mp4")

# Deteccion de objetos con camara ESTABLE
# Cambiando el tamaño del historial podemos tener mejores resultados (Camara estatica )
# Tambien modificaremos el umbral entre menor sea mas deteccion tendremos (Falsos positivos)
# Extrae los objetos en movimiento de una camara estable
deteccion = cv2.createBackgroundSubtractorMOG2(history=10000, varThreshold=12)


while True:
    ret, frame = cap.read()
    if frame is not None:
        frame = cv2.resize(frame, (1280, 720))  # Redimencionar del video
    else:
        print('No se pudo redimencionar el video, no se pudo leer la entrada')
        break

    # Elegimos una zona de interes para contar el paso de autos
    zona = frame[530: 720, 300:850]

    # Creamos una mascara a los fotogramas con el fin de que nuestros objetos sean blancos y el fondo negro
    mascara = deteccion.apply(zona)
    _, mascara = cv2.threshold(mascara, 254, 255, cv2.THRESH_BINARY)
    contornos, _ = cv2.findContours(
        mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detecciones = []  # lista de almacenamiento de la info

    # Dibujamos todos los contornos en frame, de azul claro con 2 de grosor
    for cont in contornos:
        # Eliminamos los contornos pequeños
        area = cv2.contourArea(cont)
        if area > 800:  # si el area es mayor a 100 pixeles
            # cv2.drawContours(zona,[cont], -1, (255, 255, 0), 2)
            x, y, ancho, alto = cv2.boundingRect(cont)
            cv2.rectangle(zona, (x, y), (x + ancho, y + alto),
                          (255, 255, 0), 3)  # dibujamos el rectangulo
            # Almacenamos la informacion de las detecciones
            detecciones.append([x, y, ancho, alto])
