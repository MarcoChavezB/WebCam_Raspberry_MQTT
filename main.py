import cv2

# Puerto de la webcam (por ejemplo, /dev/video1)
webcam_port = 1

# Inicializar la captura de la webcam
cap = cv2.VideoCapture(webcam_port)

# Verificar si la captura se abrió correctamente
if not cap.isOpened():
    print("Error al abrir la cámara")
    exit()

# Capturar una imagen
ret, frame = cap.read()

# Verificar si la captura fue exitosa
if ret:
    # Mostrar la imagen capturada
    cv2.imshow('Captura de Webcam', frame)
    # Guardar la imagen capturada en un archivo (por ejemplo, "captura.jpg")
    cv2.imwrite('captura.jpg', frame)
else:
    print("Error al capturar la imagen")

# Esperar a que se presione una tecla para salir
cv2.waitKey(0)

# Liberar la captura y cerrar la ventana
cap.release()
cv2.destroyAllWindows()
