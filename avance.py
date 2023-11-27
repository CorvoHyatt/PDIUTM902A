from skimage import io

# Lee la imagen desde el archivo
imagen = io.imread('imagenes/early_blight/1.jpg')
# Muestra la imagen
io.imshow(imagen)

# Espera hasta que se cierre la ventana de visualización
io.show()