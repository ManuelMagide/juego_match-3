import pygame
from pygame.locals import *
from constantes import *
import csv
import os

pygame.init()


def guardar_puntaje(nombre, puntaje, archivo_csv='puntajes.csv'):
    """
    Guarda el nombre y puntaje en un archivo CSV.
    
    parametros:
        nombre (str): Nombre del jugador (3 letras)
        puntaje (int): Puntaje obtenido en la partida
        archivo_csv (str): Nombre del archivo CSV donde guardar los datos
    """
    archivo_existe = os.path.isfile(archivo_csv)
    
    try:
        with open(archivo_csv, 'a', newline='') as archivo:
            escritor = csv.writer(archivo)
            
            # Si el archivo no existe, escribir encabezados
            if not archivo_existe:
                escritor.writerow(['Nombre', 'Puntaje'])
            
            # Escribir los datos
            escritor.writerow([nombre, puntaje])
    except Exception as e:
        print(f"Error al guardar el puntaje: {e}")


def mostrar_leaderboard(ancho_alto_pantalla, archivo_csv='puntajes.csv'):
    """
    Muestra el leaderboard de puntajes en pantalla.
    
    Args:
        ancho_alto_pantalla (tuple): Dimensiones de la pantalla (ancho, alto)
        archivo_csv (str): Nombre del archivo CSV con los puntajes
    
    Returns:
        str: 'menu_principal' cuando se cierra la pantalla
    """
    fuente_titulo = pygame.font.SysFont('Impact', 50)
    fuente_normal = pygame.font.SysFont('Impact', 30)
    
    pantalla = pygame.display.set_mode(ancho_alto_pantalla)
    pygame.display.set_caption('MATCH-3 - Leaderboard')
    
    fondo = pygame.image.load('imagenes\\FONDOS\\FONDO_MENU.png')
    fondo = pygame.transform.scale(fondo, ancho_alto_pantalla)
    
    # Cargar puntajes del CSV
    puntajes_data = []
    if os.path.isfile(archivo_csv):
        try:
            with open(archivo_csv, 'r', newline='') as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    puntajes_data.append({
                        'nombre': fila['Nombre'],
                        'puntaje': int(fila['Puntaje'])
                    })
        except Exception as e:
            print(f"Error al cargar puntajes: {e}")
    
    # Ordenar puntajes de mayor a menor
    puntajes_data.sort(key=lambda x: x['puntaje'], reverse=True)
    
    # Mantener solo los top 10
    puntajes_data = puntajes_data[:10]
    
    correr = True
    
    while correr:
        pantalla.blit(fondo, (0, 0))
        
        # Título
        titulo = fuente_titulo.render('LEADERBOARD', True, ('yellow'))
        pantalla.blit(titulo, ((ancho_alto_pantalla[0] // 2) - 200, 50))
        
        # Encabezados
        encabezado_pos = 150
        encabezado_nombre = fuente_normal.render('Nombre', True, ('cyan'))
        encabezado_puntaje = fuente_normal.render('Puntaje', True, ('cyan'))
        pantalla.blit(encabezado_nombre, (300, encabezado_pos))
        pantalla.blit(encabezado_puntaje, (700, encabezado_pos))
        
        # Mostrar puntajes
        y_pos = encabezado_pos + 60
        espaciado = 50
        
        if puntajes_data:
            for idx, dato in enumerate(puntajes_data, 1):
                # Posición del ranking
                posicion = fuente_normal.render(f'{idx}.', True, ('white'))
                pantalla.blit(posicion, (200, y_pos))
                
                # Nombre
                nombre_texto = fuente_normal.render(dato['nombre'], True, ('lime'))
                pantalla.blit(nombre_texto, (300, y_pos))
                
                # Puntaje
                puntaje_texto = fuente_normal.render(str(dato['puntaje']), True, ('orange'))
                pantalla.blit(puntaje_texto, (700, y_pos))
                
                y_pos += espaciado
        else:
            sin_puntajes = fuente_normal.render('No hay puntajes registrados', True, ('white'))
            pantalla.blit(sin_puntajes, ((ancho_alto_pantalla[0] // 2) - 200, 300))
        
        # Instrucción para salir
        instruccion = fuente_normal.render('Presiona ESC para volver al menú', True, ('white'))
        pantalla.blit(instruccion, ((ancho_alto_pantalla[0] // 2) - 300, ancho_alto_pantalla[1] - 100))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                correr = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    correr = False
        
        pygame.display.update()
    
    pygame.quit()
    return 'menu_principal'