from PIL import Image, ImageDraw, ImageFont
import uuid

def generate_objective_circle(color_circle, color_text, text):
    # Tamaño del círculo en centímetros
    diametro_cm = 0.825

    # Resolución deseada en píxeles por pulgada (PPI)
    ppi = 300  # Por ejemplo, 300 PPI para una buena calidad de impresión

    # Convertir el tamaño del círculo de centímetros a píxeles
    radio_px = int(diametro_cm * ppi / 2.54)
    diametro_px = radio_px * 2

    # Crea una nueva imagen con fondo transparente y alta resolución
    imagen = Image.new('RGBA', (diametro_px, diametro_px), (255, 255, 255, 0))
    dibujo = ImageDraw.Draw(imagen)

    # Calcula el rectángulo que define el círculo
    rectangulo = [(radio_px - radio_px, radio_px - radio_px), (radio_px + radio_px, radio_px + radio_px)]

    # Convertir el color hexadecimal al formato adecuado
    color_rgb = tuple(int(color_circle[i:i+2], 16) for i in (0, 2, 4))

    # Dibuja un círculo en la imagen
    dibujo.ellipse(rectangulo, fill=color_rgb)

    # Carga la fuente Arial en negrita con tamaño 21.5
    fuente = ImageFont.truetype("ariblk.ttf", 100)

    # Dibuja el texto en el centro del círculo
    dibujo.text((30,30), text, fill=tuple(int(color_text[i:i+2], 16) for i in (0, 2, 4)), font=fuente)

    # Guarda la imagen con la resolución especificada
    filename = "{}.png".format(uuid.uuid4())
    imagen.save(filename, dpi=(ppi, ppi))

    return filename

# Ejemplo de uso
nombre_archivo = generate_objective_circle("FFFFFF", "013AA7", "02")
print("Imagen generada:", nombre_archivo)
