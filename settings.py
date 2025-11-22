import pygame
from pygame.locals import *
from constantes import *
from funciones_utiles import *

pygame.init()

def mostrar_ajustes(ancho_alto_pantalla):
    """
    Muestra los ajustes del juego, en este caso un cambio de resoluciones.
    
    parametros:
        ancho_alto_pantalla (tupla): Dimensiones de la pantalla (ancho, alto)
    return:
        menu_principal (str): Cuando se presiona el boton de volver, nos lleva a la pantalla del menu principal
        ajustes (str): Cuando se selecciona una resolucion, nos lleva a la misma pantalla de ajustes
        nueva_res (tupla): Nueva resolucion seleccionada por el usuario
    """

    pantalla = pygame.display.set_mode(ancho_alto_pantalla)
    pygame.display.set_caption('MATCH-3')
    size_fuente = int(ancho_alto_pantalla[1] * 0.1)
    fuente = pygame.font.SysFont('Impact', size_fuente)

    volver, volver_image, boton_x, boton_volver_y = generar_imagen(pantalla, 0.1, 0.1, 150, 0.05, 'imagenes\BOTONES_EXTRAS\VUELVE.png')
    res_1200, res_1200_image, boton_res_1200_x, boton_res_1200_y = generar_imagen(pantalla, 0.2, 0.1, 2, 0.7, 'res\Res1.png')
    res_1000, res_1000_image, boton_res_1000_x, boton_res_1000_y = generar_imagen(pantalla, 0.2, 0.1, 2, 0.5, 'res\Res2.png')
    res_900, res_900_image, boton_res_900_x, boton_res_900_y = generar_imagen(pantalla, 0.2, 0.1, 2, 0.3, 'res\Res3.png')

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
        
        pantalla.blit(res_1200_image, (boton_res_1200_x, boton_res_1200_y))
        pantalla.blit(res_1000_image, (boton_res_1000_x, boton_res_1000_y))
        pantalla.blit(res_900_image, (boton_res_900_x, boton_res_900_y))
        pantalla.blit(volver_image, (boton_x, boton_volver_y))
        
        texto = fuente.render('Ajustes', True, 'White')
        boton_x_texto = (pantalla.get_width() - texto.get_width()) / 2
        pantalla.blit(texto, (boton_x_texto, boton_volver_y * 0.5))

        if DEBUG == True:
            pygame.draw.rect(pantalla, "darkorchid", volver, 1, border_radius=15)
            pygame.draw.rect(pantalla, "darkorchid", res_1200, 1, border_radius=15)
            pygame.draw.rect(pantalla, "darkorchid", res_1000, 1, border_radius=15)
            pygame.draw.rect(pantalla, "darkorchid", res_900, 1, border_radius=15)

        pygame.display.update()
    pygame.quit()