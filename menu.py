import pygame
from constantes import *
from pygame.locals import *
from funciones_utiles import *


pygame.init()

def mostrar_menu(ancho_alto_pantalla):
    """
    Muestra el menu con las distintas opciones.
    
    parametros:
        ancho_alto_pantalla(tupla): Dimensiones de la pantalla (ancho, alto)
    return:
        nivel(str): Si se selecciona jugar, te lleva a la pantalla del nivel
        leaderboard(str): Si se selecciona leaderboard, te lleva a la pantalla de leaderboard
        ajustes(str): Si se selecciona ajustes, te lleva a la pantalla de ajustes
        exit(str): Si se selecciona exit, cierra el juego
    """

    pantalla = pygame.display.set_mode(ancho_alto_pantalla)
    pygame.display.set_caption('MATCH-3')
    size_fuente = int(ancho_alto_pantalla[1] * 0.1)
    fuente = pygame.font.SysFont('Impact', size_fuente)

    jugar, play_image, boton_x, boton_jugar_y = generar_imagen(pantalla, 0.2, 0.1, 2, 0.4, 'imagenes\INTERFAZ\EWGAME.png')
    leaderboard, leaderboard_image, boton_x, boton_puntajes_y = generar_imagen(pantalla, 0.2, 0.1, 2, 0.5, 'imagenes\INTERFAZ\LEADERBOARD.png')
    settings, settings_image, boton_x, boton_settings_y = generar_imagen(pantalla, 0.2, 0.1, 2, 0.6, 'imagenes\INTERFAZ\SETT.png')
    exit, exit_image, boton_x, boton_salir_y = generar_imagen(pantalla, 0.2, 0.1, 2, 0.7, 'imagenes\INTERFAZ\EXIT.png')

    pygame.mixer.music.load("musica\Patricio_Rey_y_sus_Redonditos_de_Ricota_-_Musica_para_las_pastillas_(mp3.pm).mp3")
    pygame.mixer.music.play(1)
    pygame.mixer.music.set_volume(0.05)

    fondo = pygame.image.load('imagenes\FONDOS\FONDO_MENU.png')
    fondo = pygame.transform.scale(fondo, ancho_alto_pantalla)
    
    correr = True
    while correr:
        
        pantalla.blit(fondo, (0,0))
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                correr = False
                
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if jugar.collidepoint(mouse_pos):
                    return "nivel"
                if leaderboard.collidepoint(mouse_pos):
                    return "leaderboard"
                if settings.collidepoint(mouse_pos):
                    return "ajustes"
                if exit.collidepoint(mouse_pos):
                    return "exit"

        titulo = fuente.render("Match-3", True, ('white'))
        titulo_rect = titulo.get_rect(center=(ancho_alto_pantalla[0] // 2, ancho_alto_pantalla[1] // 5))
        pantalla.blit(titulo, titulo_rect)
        
        pantalla.blit(play_image, (boton_x, boton_jugar_y))
        pantalla.blit(leaderboard_image, (boton_x, boton_puntajes_y))
        pantalla.blit(settings_image, (boton_x, boton_settings_y))
        pantalla.blit(exit_image, (boton_x, boton_salir_y))

        if DEBUG == True:
            pygame.draw.rect(pantalla, "darkorchid", jugar, 1, border_radius=15)
            pygame.draw.rect(pantalla, "darkorchid", titulo_rect, 1, border_radius=15)
            pygame.draw.rect(pantalla, "darkorchid", leaderboard, 1, border_radius=15)
            pygame.draw.rect(pantalla, "darkorchid", settings, 1, border_radius=15)
            pygame.draw.rect(pantalla, "darkorchid", exit, 1, border_radius=15)
        
        pygame.display.update()
    pygame.quit()