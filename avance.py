import cv2

# Lee la imagen desde el archivo
img = cv2.imread("imagenes/early_blight/1.jpg",0)

# Muestra la imagen en una ventana
cv2.imshow('Imagen', img)

# Espera hasta que se presione una tecla (0 significa esperar indefinidamente)
cv2.waitKey(0)

# Cierra todas las ventanas
cv2.destroyAllWindows()