import pygame
from menu import *
from nivel import *
from puntajes import *
from leaderboard import *
from settings import *
from constantes import *

def main():
    pygame.init()

    estado = "menu_principal"
    bandera_ajustes = True
    
    correr = True
    while correr:
        
        if estado == "menu_principal":
            if bandera_ajustes == True:
                estado = mostrar_menu(PANTALLA)
            elif estado == 'menu_principal' and bandera_ajustes == False:
                estado = mostrar_menu(nueva_res)
        elif estado == "nivel":
            if bandera_ajustes == True:
                estado = nivel(PANTALLA)
            elif estado == 'nivel' and bandera_ajustes == False:
                estado = nivel(nueva_res)
        elif estado == 'ajustes':
            if bandera_ajustes == True:
                estado, nueva_res = mostrar_ajustes(PANTALLA)
                bandera_ajustes = False
            elif estado == 'ajustes' and bandera_ajustes == False:
                estado, nueva_res = mostrar_ajustes(nueva_res)
        elif estado == "leaderboard":
            if bandera_ajustes == True:
                estado = mostrar_leaderboard(PANTALLA, 'puntajes.csv')
            elif estado == 'leaderboard' and bandera_ajustes == False:
                estado = mostrar_leaderboard(nueva_res, 'puntajes.csv')
        elif estado == "exit":
            correr = False
            break
    pygame.quit()

main()