import pygame
from constantes import *
from pygame.locals import *

pygame.init()

'''def saber_top10(lista):
    lista = []
    return lista'''

def leaderboard(ancho_alto_pantalla):

    size_fuente = int(ancho_alto_pantalla[1] * 0.1)
    fuente = pygame.font.SysFont('Impact', size_fuente)
    pantalla = pygame.display.set_mode(ancho_alto_pantalla)
    pygame.display.set_caption('MATCH-3')

    boton_ancho = pantalla.get_width() * 0.1
    boton_alto = pantalla.get_height() * 0.1
    boton_x = (pantalla.get_width() - boton_ancho) / 150
    boton_volver_y = pantalla.get_height() * 0.05

    fondo = pygame.image.load('imagenes\FONDOS\FONDO_MENU.png')
    fondo = pygame.transform.scale(fondo, ancho_alto_pantalla)

    '''puntajes = saber_top10()'''

    correr = True

    while correr:

        pantalla.blit(fondo, (0,0))
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                correr = False

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if volver.collidepoint(mouse_pos):
                    return "menu_principal"

        volver = pygame.Rect(boton_x, boton_volver_y, boton_ancho, boton_alto)
        volver_image = pygame.image.load('imagenes\BOTONES_EXTRAS\VUELVE.png')
        volver_image = pygame.transform.scale(volver_image, (boton_ancho, boton_alto))
        pantalla.blit(volver_image, (boton_x, boton_volver_y))

        texto = fuente.render('Top10', True, 'White')
        pantalla.blit(texto, (boton_x * 65, boton_volver_y * 0.5))

        if DEBUG == True:
            pygame.draw.rect(pantalla, "darkorchid", volver, 1, border_radius=15)

        pygame.display.update()

    pygame.quit()