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
            matriz[i][j] = {"objeto": lista_valores[indice_aleatorio]}

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
    boton_ancho = pantalla.get_width() * 0.1
    boton_alto = pantalla.get_height() * 0.12
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            objeto_image = pygame.image.load(matriz[i][j]["objeto"])
            objeto_image = pygame.transform.scale(objeto_image, (boton_ancho, boton_alto))
            pantalla.blit(objeto_image, matriz[i][j]["rect"])

            if DEBUG == True:
                pygame.draw.rect(pantalla, "darkorchid", matriz[i][j]["rect"], 1, border_radius=15)

def nivel(ancho_alto_pantalla):

    lista_colores = ["imagenes\ICONS\DIENTE.png", 
                    "imagenes\ICONS\FRUTA_V.png",
                    "imagenes\ICONS\HUEVO.png",
                    "imagenes\ICONS\OJO.png",
                    "imagenes\ICONS\ROSA.png",
                    "imagenes\ICONS\HOJA.png"]
    matriz = inicializar_matriz(8, 8)
    cargar_matriz_aleatoria(matriz, lista_colores)

    pantalla = pygame.display.set_mode(ancho_alto_pantalla)
    pygame.display.set_caption('MATCH-3')
    size_fuente = int(ancho_alto_pantalla[1] * 0.1)
    fuente = pygame.font.SysFont('Impact', size_fuente)

    boton_ancho = pantalla.get_width() * 0.1
    boton_alto = pantalla.get_height() * 0.1
    boton_x = (pantalla.get_width() - boton_ancho) / 150
    boton_volver_y = pantalla.get_height() * 0.05

    margen_y = pantalla.get_height() * 0.001
    alto_rc = pantalla.get_height() - (margen_y * 2)
    margen_x = pantalla.get_width() - alto_rc - (pantalla.get_width() * 0.01)
    rectangulo_contenedor = pygame.Rect(margen_x, margen_y, alto_rc, alto_rc)
    generar_rectangulos(matriz, rectangulo_contenedor)

    fondo = pygame.image.load('imagenes\FONDOS\FONDO_MENU.png')
    fondo = pygame.transform.scale(fondo, ancho_alto_pantalla)

    corriendo = True

    while corriendo == True:
        
        pantalla.blit(fondo, (0,0))
        mouse_pos = pygame.mouse.get_pos()
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if volver.collidepoint(mouse_pos):
                    return "menu_principal"
            if evento.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(matriz)):
                    for j in range(len(matriz[i])):
                        if matriz[i][j]["rect"].collidepoint(evento.pos) == True:
                            print(f"Apretaste sobre celda {i} - {j}")
                            matriz[i][j]["objeto"] = "black"

        volver = pygame.Rect(boton_x, boton_volver_y, boton_ancho, boton_alto)
        volver_image = pygame.image.load('imagenes\BOTONES_EXTRAS\VUELVE.png')
        volver_image = pygame.transform.scale(volver_image, (boton_ancho, boton_alto))
        pantalla.blit(volver_image, (boton_x, boton_volver_y))

        pygame.draw.rect(pantalla, "black", rectangulo_contenedor)
        dibujar_matriz(matriz, pantalla)

        if DEBUG == True:
            pygame.draw.rect(pantalla, "darkorchid", volver, 1, border_radius=15)

        pygame.display.flip()
