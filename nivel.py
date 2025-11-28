import pygame
import random
from constantes import *
from pygame.locals import *
from puntajes import *
from funciones_utiles import *

def inicializar_matriz(cant_filas:int, cant_columnas:int, valor_inicial:any=None)->list[list]:
    """
    Inicializa una matriz armada mediante listas y nosotros elegimos su formato.
    
    parametros:
        cant_filas (int): Cantidad de filas que tendra la matriz
        cant_columnas (int): Cantidad de columnas que tendra la matriz
        valor_inicial (any): Valor con el que se inicializan las posiciones de la matriz
    return:
        matriz (list[list]): Matriz inicializada con el valor inicial en todas sus posiciones
    """
    matriz = []
    for _ in range(cant_filas):
        fila = []
        for _ in range(cant_columnas):
            fila.append(valor_inicial)
        matriz.append(fila)
    return matriz

def cargar_matriz_aleatoria(matriz:list[list], lista_valores:list)->None:
    """
    Carga la matriz que generamos y le da valores aleatorios a los distintos indices.
    Crea una matriz de diccionarios, agregandoles la clave "imagen" con el valor correspondiente.
    
    parametros:
        matriz (list[list]): Matriz que vamos a cargar
        lista_valores (list): Lista con los valores que puede tomar cada posicion de la matriz
    return:
        None
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            indice_aleatorio = random.randint(0, len(lista_valores) - 1)
            matriz[i][j] = {"imagen": lista_valores[indice_aleatorio]}

def generar_rectangulos(matriz:list[list], rect_contenedor:pygame.Rect)->None:
    """
    Genera la hitbox, agregandole la clave "rect", con su respectivo valor, a cada posicion de la matriz.
    
    parametros:
        matriz (list[list]): Matriz que vamos a cargar
        rect_contenedor (pygame.Rect): Rectangulo que contiene a toda la matriz
    return:
        None
    """
    ancho_celda = int(rect_contenedor.width / len(matriz[0]) * 0.98)
    alto_celda = int(rect_contenedor.height / len(matriz) * 0.98)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            un_rect_x = (j * ancho_celda) + rect_contenedor.x + (rect_contenedor.width * 0.01) + j
            un_rect_y = (i * alto_celda) + rect_contenedor.y + (rect_contenedor.height * 0.01) + i
            un_rect = pygame.Rect(un_rect_x, un_rect_y, ancho_celda, alto_celda)
            matriz[i][j].update({"rect": un_rect})

def generar_estado(matriz:list[list])->None:
    """
    Genera el estado, agregandole la clave "estado", por defecto False, a cada posicion de la matriz.
    
    parametros:
        matriz (list[list]): Matriz que vamos a cargar
    return:
        None
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            estado = False
            matriz[i][j].update({"estado": estado})

def dibujar_matriz(matriz:list[list], pantalla:pygame.Surface)->None:
    """
    Carga y dibuja la matriz en la pantalla.
    
    parametros:
        matriz (list[list]): Matriz que vamos a cargar
        pantalla(surface): Superficie donnde se dibuja la imagen
    return:
        None
    """
    boton_ancho = pantalla.get_width() * 0.1
    boton_alto = pantalla.get_height() * 0.12
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            image = pygame.image.load(matriz[i][j]["imagen"])
            image = pygame.transform.scale(image, (boton_ancho, boton_alto))
            pantalla.blit(image, matriz[i][j]["rect"])

def nivel(ancho_alto_pantalla):
    """
    Carga el nivel del juego y ejecuta el resto de funciones de matriz para generarla.
    
    parametros:
        ancho_alto_pantalla (tupla): Dimensiones de la pantalla (ancho, alto)
    return:
        menu_principal (str): Cuando se presiona el boton de volver, nos lleva a la pantalla del menu principal
    """

    lista_image = ["imagenes\ICONS\DIENTE.png", 
                    "imagenes\ICONS\FRUTA_V.png",
                    "imagenes\ICONS\HUEVO.png",
                    "imagenes\ICONS\OJO.png",
                    "imagenes\ICONS\ROSA.png",
                    "imagenes\ICONS\HOJA.png"]
    matriz = inicializar_matriz(8, 8)
    cargar_matriz_aleatoria(matriz, lista_image)

    pantalla = pygame.display.set_mode(ancho_alto_pantalla)
    pygame.display.set_caption('MATCH-3')
    size_fuente = int(ancho_alto_pantalla[1] * 0.1)
    fuente = pygame.font.SysFont('Impact', size_fuente)

    volver, volver_image, boton_x, boton_volver_y = generar_imagen(pantalla, 0.1, 0.1, 150, 0.05, 'imagenes\BOTONES_EXTRAS\VUELVE.png')

    margen_y = pantalla.get_height() * 0.001
    alto_rc = pantalla.get_height() - (margen_y * 2)
    margen_x = pantalla.get_width() - alto_rc - (pantalla.get_width() * 0.01)
    rectangulo_contenedor = pygame.Rect(margen_x, margen_y, alto_rc, alto_rc)
    generar_rectangulos(matriz, rectangulo_contenedor)
    generar_estado(matriz)

    fondo = pygame.image.load('imagenes\FONDOS\FONDO_MENU.png')
    fondo = pygame.transform.scale(fondo, ancho_alto_pantalla)

    corriendo = True
    aux_estado = False
    primer_click = None  
    segundo_click = None 

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

                        if matriz[i][j]["rect"].collidepoint(evento.pos):

                            if primer_click is None:
                                primer_click = (i, j)
                                matriz[i][j]["estado"] = True
                                aux_rect = matriz[i][j]["rect"]
                                aux_estado = matriz[i][j]["estado"]

                            elif segundo_click is None:
                                segundo_click = (i, j)
                                matriz[i][j]["estado"] = True

                                i1, j1 = primer_click #i es fila(y), j es columna(x)
                                i2, j2 = segundo_click

                                if (i1 - i2 == 0) or (j1 - j2 == 0):
                                    if(i1 - i2 == 1 or i1 - i2 == -1) or (j1 - j2 == 1 or j1 - j2 == -1):

                                        pos1 = matriz[i1][j1]["rect"].topleft
                                        pos2 = matriz[i2][j2]["rect"].topleft

                                        matriz[i1][j1], matriz[i2][j2] = matriz[i2][j2], matriz[i1][j1]

                                        matriz[i1][j1]["rect"].topleft = pos1
                                        matriz[i2][j2]["rect"].topleft = pos2

                                        if ((matriz[i1][j1]["imagen"] == matriz[i1+1][j1]["imagen"] and matriz[i1][j1]["imagen"] == matriz[i1+2][j1]["imagen"]) or
                                        (matriz[i1][j1]["imagen"] == matriz[i1-1][j1]["imagen"] and matriz[i1][j1]["imagen"] == matriz[i1-2][j1]["imagen"]) or
                                        (matriz[i1][j1]["imagen"] == matriz[i1][j1+1]["imagen"] and matriz[i1][j1]["imagen"] == matriz[i1][j1+2]["imagen"]) or
                                        (matriz[i1][j1]["imagen"] == matriz[i1][j1-1]["imagen"] and matriz[i1][j1]["imagen"] == matriz[i1][j1-2]["imagen"])):
                                            
                                            print("Hay match")

                                            matriz[i1][j1]["estado"] = False
                                            matriz[i2][j2]["estado"] = False

                                        primer_click = None
                                        segundo_click = None
                                        aux_estado = False
                                    else:
                                        matriz[i][j]["estado"] = False
                                        segundo_click = None
                                else:
                                        matriz[i][j]["estado"] = False
                                        segundo_click = None

        pantalla.blit(volver_image, (boton_x, boton_volver_y))

        pygame.draw.rect(pantalla, "black", rectangulo_contenedor)
        dibujar_matriz(matriz, pantalla)
        if aux_estado == True:
            pygame.draw.rect(pantalla, "green", aux_rect, 3, border_radius=15)

        if DEBUG == True:
            pygame.draw.rect(pantalla, "darkorchid", volver, 1, border_radius=15)
        pygame.display.flip()

nivel(PANTALLA)