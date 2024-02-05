from PIL import Image, ImageDraw, ImageFont

def agregar_texto_porcentaje(color_img, color_text, texto_completo):
    """
    Añade un texto completo a una imagen.

    Parámetros:
    - imagen: Ruta de la imagen PNG.
    - texto_completo: Texto completo que se agregará a la imagen.
    """
    # Abrir la imagen

    r = int(color_img[0:2], 16)
    g = int(color_img[2:4], 16)
    b = int(color_img[4:6], 16)

    new_color = (r, g, b)

    img = Image.open('img_beneficios.png')

    # Obtener el tamaño de la imagen
    datos_pixeles = img.load()

    ancho, alto = img.size

    for i in range(ancho):
        for j in range(alto):
            # Verificar si el píxel es blanco
            if datos_pixeles[i, j] == (255, 255, 255, 255):
                # Cambiar el color del píxel
                datos_pixeles[i, j] = new_color

    # Crear un objeto ImageDraw para dibujar en la imagen
    dibujo = ImageDraw.Draw(img)

    # Especificar la fuente y el tamaño del texto
    fuente = ImageFont.truetype("arialbd.ttf", 50)

    coordenadas = (0, 0)

    if (len(texto_completo) == 4):
        coordenadas = (17, 30)
    elif (len(texto_completo) == 3):
        coordenadas = (33, 30)
    else:
        coordenadas = (45, 30)


    # Dibujar el texto en la imagen
    dibujo.text(coordenadas, texto_completo, fill=tuple(int(color_text[i:i+2], 16) for i in (0, 2, 4)), font=fuente)

    # Guardar la imagen modificada
    filename = "{}.png".format(uuid.uuid4())
    img.save(filename, dpi=(ppi, ppi))

    return filename

# Ejemplo de uso
agregar_texto_porcentaje("013AA7", "FFFFFF", "100%")  # Añade "100%" a la imagen
