import pygame
from pygame.locals import *
from constantes import *
import csv
import os

pygame.init()


def guardar_puntaje(nombre, puntaje, primera_entrada, archivo_csv='puntajes.csv'):
    """
    Guarda el nombre y puntaje en un archivo CSV, si el puntaje es mas alto y se repite el nombre, se queda el mas alto.
    
    parametros:
        nombre (str): Nombre del jugador
        puntaje (int): Puntaje obtenido en la partida
        primera_entrada (bool): Indica si es la primera vez que se guarda un puntaje
        archivo_csv (str): Nombre del archivo CSV donde guardar los datos
    """

    columnas = ['Nombre', 'Puntaje']
    matriz_datos = []

    if primera_entrada == True:
        with open(archivo_csv, 'w') as archivo:
            archivo.write(','.join(columnas) + '\n')
    else:
        with open(archivo_csv, 'r') as archivo:
            lineas = archivo.readlines()
        
        for i in range(1, len(lineas)):
            datos = lineas[i].strip().split(',')
            if len(datos) == 2:
                matriz_datos.append([datos[0], int(datos[1])])
    
    jugador_encontrado = False
    for fila in matriz_datos:
        if fila[0] == nombre:
            jugador_encontrado = True
            if puntaje > fila[1]: 
                fila[1] = puntaje
            break

    if not jugador_encontrado:
        matriz_datos.append([nombre, puntaje])
    
    with open(archivo_csv, 'w') as archivo:
        archivo.write("Nombre,Puntaje\n")
        for fila in matriz_datos:
            archivo.write(f"{fila[0]},{fila[1]}\n")
