import pygame
import random
from constantes import *
from pygame.locals import *
from puntajes import *

def inicializar_matriz(cant_filas:int, cant_columnas:int, valor_inicial:any=None)->list[list]:
        matriz = []
        for _ in range(cant_filas):
            fila = []
            for _ in range(cant_columnas):
                fila.append(valor_inicial)
            matriz.append(fila)
        return matriz

def cargar_matriz_aleatoria(matriz:list[list], lista_valores:list)->None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            indice_aleatorio = random.randint(0, len(lista_valores) - 1)
            matriz[i][j] = {"color": lista_valores[indice_aleatorio]}

def generar_rectangulos(matriz:list[list], rect_contenedor:pygame.Rect)->None:
    ancho_celda = int(rect_contenedor.width / len(matriz[0]) * 0.98)
    alto_celda = int(rect_contenedor.height / len(matriz) * 0.98)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            un_rect_x = (j * ancho_celda) + rect_contenedor.x + (rect_contenedor.width * 0.01) + j
            un_rect_y = (i * alto_celda) + rect_contenedor.y + (rect_contenedor.height * 0.01) + i
            un_rect = pygame.Rect(un_rect_x, un_rect_y, ancho_celda, alto_celda)
            matriz[i][j].update({"rect": un_rect})

def dibujar_matriz(matriz:list[list], pantalla:pygame.Surface)->None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            pygame.draw.rect(pantalla, matriz[i][j]["color"], matriz[i][j]["rect"])
            # Si queremos dibujar imagenes, usamos pantalla.blit()

def nivel():
    pygame.display.set_caption('MATCH-3')

    lapida = pygame.image.load('Imagenes\soss\Tombstone1.png')
    header = pygame.image.load('Imagenes\menu sprites\PNG\You_Lose\Window.png')
    win = pygame.image.load('Imagenes\menu sprites\PNG\You_Win\Header.png')
    lose = pygame.image.load('Imagenes\menu sprites\PNG\You_Lose\Header.png')
    stars = pygame.image.load('Imagenes\menu sprites\PNG\You_Lose\Star_01.png')
    score = pygame.image.load('Imagenes\menu sprites\PNG\You_Lose\Score.png')
    play_again = pygame.image.load('Imagenes\menu sprites\PNG\You_Lose\Replay_BTN.png')
    volver_menu = pygame.image.load('Imagenes\menu sprites\PNG\Level_Menu\Hangar_BTN.png')
    stars_win = pygame.image.load('Imagenes\menu sprites\PNG\You_Lose\Star_03.png')
    guardar_puntos = pygame.image.load('Imagenes\menu sprites\PNG\Rating\Ok_BTN.png')

    lose = pygame.transform.scale(lose, (175, 50))
    win = pygame.transform.scale(win, (175, 50))
    header = pygame.transform.scale(header, (PANTALLA[0] // 2, PANTALLA[1] // 2))
    stars = pygame.transform.scale(stars, (75, 75))
    stars_win = pygame.transform.scale(stars_win, (75, 75))
    score = pygame.transform.scale(score, (100, 50))
    play_again = pygame.transform.scale(play_again, (75, 75))
    volver_menu = pygame.transform.scale(volver_menu, (75, 75))
    guardar_puntos = pygame.transform.scale(guardar_puntos, (75, 75))

    bandera_tiempo = True
    aux_tiempo = 1
    tiempo_regresivo = 100 
    bandera_disparo_2 = False
    bandera_disparo_3 = False
    dejar_item_1 = False
    dejar_item_2 = False
    dejar_disparo_2 = False
    dejar_disparo_3 = False
    dejar_curacion = False
    bandera_boss = True
    bandera_win = False
    bandera_lose = False

    pygame.mixer.music.load("Sonidos\- Overworld Day.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.05)

    sfx_channel = pygame.mixer.Channel(1)
    sfx_channel_2 = pygame.mixer.Channel(2)
    sfx_channel_4 = pygame.mixer.Channel(4)
    sfx_channel_5 = pygame.mixer.Channel(5)

    fuente = pygame.font.SysFont('Impact', 30)

    fondo = pygame.image.load('Imagenes\Fondo.jpg')
    fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))

    '''for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if bandera_win == True or bandera_lose == True:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if volver.collidepoint(mouse_pos):
                        return "menu_principal", dic_puntaje
                    if replay.collidepoint(mouse_pos):
                        return "nivel", dic_puntaje
                    if guardar.collidepoint(mouse_pos):
                        if len(dic_puntaje) <= 0:
                            dic_puntaje['puntaje'] = 0
                            return 'guardar_puntaje',dic_puntaje
                        else:
                            return 'guardar_puntaje',dic_puntaje'''