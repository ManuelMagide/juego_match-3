import pygame
from pygame.locals import *
from constantes import *

pygame.init()

def mostrar_ajustes(ancho_alto_pantalla):

    pantalla = pygame.display.set_mode(ancho_alto_pantalla)
    pygame.display.set_caption('MATCH-3')
    size_fuente = int(ancho_alto_pantalla[1] * 0.1)
    fuente = pygame.font.SysFont('Impact', size_fuente)

    boton_ancho = pantalla.get_width() * 0.1
    boton_alto = pantalla.get_height() * 0.1
    boton_x = (pantalla.get_width() - boton_ancho) / 150
    boton_volver_y = pantalla.get_height() * 0.05

    boton_res_ancho = pantalla.get_width() * 0.2
    boton_res_alto = pantalla.get_height() * 0.1
    boton_res_x = (pantalla.get_width() - boton_ancho) / 2.2
    boton_res_y = pantalla.get_height() * 0.70

    fondo = pygame.image.load('imagenes\FONDOS\FONDO_MENU.png')
    fondo = pygame.transform.scale(fondo, ancho_alto_pantalla)

    correr = True

    while correr:

        pantalla.blit(fondo, (0,0))
        mouse_pos = pygame.mouse.get_pos()
        res = ancho_alto_pantalla

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                correr = False

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if volver.collidepoint(mouse_pos):
                    return ("menu_principal", res)
                elif res_1200.collidepoint(mouse_pos):
                    res = (1200, 1000)
                    return ('ajustes', res)
                elif res_1000.collidepoint(mouse_pos):
                    res = (1000, 800)
                    return ('ajustes', res)
                elif res_900.collidepoint(mouse_pos):
                    res = (900, 700)
                    return ('ajustes', res)
        
        res_1200 = pygame.Rect(boton_res_x, boton_res_y, boton_res_ancho, boton_res_alto)
        res_1200_image = pygame.image.load('res\Res1.png')
        res_1200_image = pygame.transform.scale(res_1200_image, (boton_res_ancho, boton_res_alto))
        pantalla.blit(res_1200_image, (boton_res_x, boton_res_y))

        res_1000 = pygame.Rect(boton_res_x, boton_res_y * 0.70, boton_res_ancho, boton_res_alto)
        res_1000_image = pygame.image.load('res\Res2.png')
        res_1000_image = pygame.transform.scale(res_1000_image, (boton_res_ancho, boton_res_alto))
        pantalla.blit(res_1000_image, (boton_res_x, boton_res_y * 0.70))

        res_900 = pygame.Rect(boton_res_x, boton_res_y * 0.40, boton_res_ancho, boton_res_alto)
        res_900_image = pygame.image.load('res\Res3.png')
        res_900_image = pygame.transform.scale(res_900_image, (boton_res_ancho, boton_res_alto))
        pantalla.blit(res_900_image, (boton_res_x, boton_res_y * 0.40))

        volver = pygame.Rect(boton_x, boton_volver_y, boton_ancho, boton_alto)
        volver_image = pygame.image.load('imagenes\BOTONES_EXTRAS\VUELVE.png')
        volver_image = pygame.transform.scale(volver_image, (boton_ancho, boton_alto))
        pantalla.blit(volver_image, (boton_x, boton_volver_y))

        texto = fuente.render('Ajustes', True, 'White')
        pantalla.blit(texto, (boton_x * 65, boton_volver_y * 0.5))

        if DEBUG == True:
            pygame.draw.rect(pantalla, "darkorchid", volver, 1, border_radius=15)
            pygame.draw.rect(pantalla, "darkorchid", res_1200, 1, border_radius=15)
            pygame.draw.rect(pantalla, "darkorchid", res_1000, 1, border_radius=15)
            pygame.draw.rect(pantalla, "darkorchid", res_900, 1, border_radius=15)

        pygame.display.update()
    pygame.quit()
