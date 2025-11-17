import pygame
from constantes import *
from pygame.locals import *

pygame.init()

def mostrar_menu(ancho_alto_pantalla):

    pantalla = pygame.display.set_mode(ancho_alto_pantalla)
    pygame.display.set_caption('MATCH-3')
    size_fuente = int(ancho_alto_pantalla[1] * 0.1)
    fuente = pygame.font.SysFont('Impact', size_fuente)

    boton_ancho = pantalla.get_width() * 0.2
    boton_alto = pantalla.get_height() * 0.1
    boton_x = (pantalla.get_width() - boton_ancho) / 2
    boton_jugar_y = pantalla.get_height() * 0.40
    boton_puntajes_y = pantalla.get_height() * 0.50
    boton_settings_y = pantalla.get_height() * 0.60
    boton_salir_y = pantalla.get_height() * 0.70

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
        
        jugar = pygame.Rect(boton_x, boton_jugar_y, boton_ancho, boton_alto)
        play_image = pygame.image.load('imagenes\INTERFAZ\EWGAME.png')
        play_image = pygame.transform.scale(play_image, (boton_ancho, boton_alto))
        pantalla.blit(play_image, (boton_x, boton_jugar_y))
        
        leaderboard = pygame.Rect(boton_x, boton_puntajes_y, boton_ancho, boton_alto)
        leaderboard_image = pygame.image.load('imagenes\INTERFAZ\LEADERBOARD.png')
        leaderboard_image = pygame.transform.scale(leaderboard_image, (boton_ancho, boton_alto))
        pantalla.blit(leaderboard_image, (boton_x, boton_puntajes_y))

        settings = pygame.Rect(boton_x, boton_settings_y, boton_ancho, boton_alto)
        settings_image = pygame.image.load('imagenes\INTERFAZ\SETT.png')
        settings_image = pygame.transform.scale(settings_image, (boton_ancho, boton_alto))
        pantalla.blit(settings_image, (boton_x, boton_settings_y))

        exit = pygame.Rect(boton_x, boton_salir_y, boton_ancho, boton_alto)
        exit_image = pygame.image.load('imagenes\INTERFAZ\EXIT.png')
        exit_image = pygame.transform.scale(exit_image, (boton_ancho, boton_alto))
        pantalla.blit(exit_image, (boton_x, boton_salir_y))

        if DEBUG == True:
            pygame.draw.rect(pantalla, "darkorchid", jugar, 1, border_radius=15)
            pygame.draw.rect(pantalla, "darkorchid", titulo_rect, 1, border_radius=15)
            pygame.draw.rect(pantalla, "darkorchid", leaderboard, 1, border_radius=15)
            pygame.draw.rect(pantalla, "darkorchid", settings, 1, border_radius=15)
            pygame.draw.rect(pantalla, "darkorchid", exit, 1, border_radius=15)
        
        pygame.display.update()
    pygame.quit()