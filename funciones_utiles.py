import pygame

def generar_imagen(pantalla, porcentaje_ancho, porcentaje_alto, porcentaje_x, porcentaje_y, imagen_cargada):
    """
    Genera, reescala la imagen que vamos a utilizar y su hitbox.
    
    parametros:
        pantalla(surface): Superficie donnde se dibuja la imagen
        porcentaje_ancho(float): Porcentaje del ancho de la imagen respecto a la pantalla
        porcentaje_alto(float): Porcentaje del alto de la imagen respecto a la pantalla
        porcentaje_x(float): Porcentaje para calcular la posicion x de la imagen
        porcentaje_y(float): Porcentaje para calcular la posicion y de la imagen
        imagen_cargada(str): Ruta de la imagen que vamos a cargar
    return:
        rect(Rect): Hitbox de la imagen
        image(surface): Imagen reescalada
        x(float): Posicion x de la imagen
        y(float): Posicion y de la imagen
    """
    ancho = pantalla.get_width() * porcentaje_ancho
    alto = pantalla.get_height() * porcentaje_alto
    x = (pantalla.get_width() - ancho) / porcentaje_x
    y = pantalla.get_height() * porcentaje_y

    rect = pygame.Rect(x, y, ancho, alto)
    image = pygame.image.load(imagen_cargada)
    image = pygame.transform.scale(image, (ancho, alto))

    return rect, image, x, y