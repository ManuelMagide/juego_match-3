import pygame

def generar_imagen(pantalla, porcentaje_ancho, porcentaje_alto, porcentaje_x, porcentaje_y, imagen_cargada):
    ancho = pantalla.get_width() * porcentaje_ancho
    alto = pantalla.get_height() * porcentaje_alto
    x = (pantalla.get_width() - ancho) / porcentaje_x
    y = pantalla.get_height() * porcentaje_y

    rect = pygame.Rect(x, y, ancho, alto)
    image = pygame.image.load(imagen_cargada)
    image = pygame.transform.scale(image, (ancho, alto))

    return rect, image, x, y