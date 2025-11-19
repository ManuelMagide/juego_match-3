import pygame
from constantes import *
from pygame.locals import *
from funciones_utiles import *

pygame.init()

'''def saber_top10(lista):
    lista = []
    return lista'''

def leaderboard(ancho_alto_pantalla):

    size_fuente = int(ancho_alto_pantalla[1] * 0.1)
    fuente = pygame.font.SysFont('Impact', size_fuente)
    pantalla = pygame.display.set_mode(ancho_alto_pantalla)
    pygame.display.set_caption('MATCH-3')

    volver, volver_image, boton_x, boton_volver_y = generar_imagen(pantalla, 0.1, 0.1, 150, 0.05, 'imagenes\BOTONES_EXTRAS\VUELVE.png')

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

        pantalla.blit(volver_image, (boton_x, boton_volver_y))

        texto = fuente.render('Top10', True, 'White')
        boton_x_texto = (pantalla.get_width() - texto.get_width()) / 2
        pantalla.blit(texto, (boton_x_texto, boton_volver_y * 0.5))

        if DEBUG == True:
            pygame.draw.rect(pantalla, "darkorchid", volver, 1, border_radius=15)

        pygame.display.update()
    pygame.quit()