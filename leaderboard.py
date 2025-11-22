import pygame
from constantes import *
from pygame.locals import *
from funciones_utiles import *

pygame.init()

def generar_top10():
    """
    Reordena el top10 del archivo csv, pasandolo a una lista.
    
    return:
        puntaje_datos (list): Lista con los 10 mejores puntajes y sus respectivos nombres
    """
    puntaje_datos = []
    try:
        with open('puntajes.csv', 'r') as archivo:
            lineas = archivo.readlines()
        
        for i in range(1, len(lineas)):
            linea = lineas[i].strip()
            if linea:
                partes = linea.split(',')
                if len(partes) == 2:
                    nombre = partes[0]
                    puntaje = int(partes[1])
                    puntaje_datos.append({'nombre': nombre, 'puntaje': puntaje})
    except:
        pass
    
    n = len(puntaje_datos)
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if puntaje_datos[j]['puntaje'] < puntaje_datos[j + 1]['puntaje']:
                aux = puntaje_datos[j]
                puntaje_datos[j] = puntaje_datos[j + 1]
                puntaje_datos[j + 1] = aux
            j = j + 1
        i = i + 1
    
    puntaje_datos = puntaje_datos[:10]
    return puntaje_datos

def leaderboard(ancho_alto_pantalla):
    """
    Muestra el leaderboard coon su top10 mejores jugadores.
    
    parametros:
        ancho_alto_pantalla(tupla): Dimensiones de la pantalla (ancho, alto)
    return:
        menu_principal (str): Cuando se presiona el boton de volver, nos lleva a la pantalla del menu principal
    """

    size_fuente = int(ancho_alto_pantalla[1] * 0.1)
    fuente = pygame.font.SysFont('Impact', size_fuente)
    size_fuente_puntajes = int(ancho_alto_pantalla[1] * 0.05)
    fuente_puntajes = pygame.font.SysFont('Impact', size_fuente_puntajes)
    
    pantalla = pygame.display.set_mode(ancho_alto_pantalla)
    pygame.display.set_caption('MATCH-3')

    volver, volver_image, boton_x, boton_volver_y = generar_imagen(pantalla, 0.1, 0.1, 150, 0.05, 'imagenes\BOTONES_EXTRAS\VUELVE.png')

    fondo = pygame.image.load('imagenes\FONDOS\FONDO_MENU.png')
    fondo = pygame.transform.scale(fondo, ancho_alto_pantalla)

    puntaje_datos = generar_top10()

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

        y_puntajes = int(ancho_alto_pantalla[1] * 0.25)
        espaciado = int(ancho_alto_pantalla[1] * 0.06)
        
        contador = 1
        for dato in puntaje_datos:
            linea_puntaje = f"{contador}. {dato['nombre']} - {dato['puntaje']}"
            puntaje_render = fuente_puntajes.render(linea_puntaje, True, 'yellow')
            x_puntajes = (pantalla.get_width() - puntaje_render.get_width()) / 2
            pantalla.blit(puntaje_render, (x_puntajes, y_puntajes))
            y_puntajes += espaciado
            contador = contador + 1

        if DEBUG == True:
            pygame.draw.rect(pantalla, "darkorchid", volver, 1, border_radius=15)

        pygame.display.update()
    pygame.quit()