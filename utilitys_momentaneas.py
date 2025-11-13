import pygame
import random

pygame.init()

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
    # primer_rect = pygame.Rect(0, 0, ancho_total / len(matriz[0]), alto_total / len(matriz))
    # segundo_rect = pygame.Rect(0 + primer_rect.width, 0, ancho_total / len(matriz[0]), alto_total / len(matriz))
    # noveno_rect = pygame.Rect(0, 0 + primer_rect.height, ancho_total / len(matriz[0]), alto_total / len(matriz))
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


TAMANIO_PANTALLA = [1200, 900]
OTRO_TAMANIO = [1200*0.85, 900*0.85]
pantalla = pygame.display.set_mode(TAMANIO_PANTALLA)

# imagen_caramelo = pygame.image.load("ruta/caramelo.jpg")
lista_colores = ["blue", "red", "green", "yellow", "purple", "lightblue"]
#lista_imagenes = [imagen_caramelo]
matriz = inicializar_matriz(8, 8)
cargar_matriz_aleatoria(matriz, lista_colores)

# Imagenes
imagen_flecha_volver = pygame.image.load("imagenes\BOTONES_EXTRAS\VUELVE.png")

# Fuentes
#print(pygame.font.get_fonts())
fuente = pygame.font.SysFont('sylfaen', 80)

# Textos (Superficies)
texto_pantalla_inicio = fuente.render("Pantalla Inicio", True, "gray7")
texto_pantalla_puntajes = fuente.render("Pantalla Puntajes", True, "gray7")
texto_boton_jugar = fuente.render("Jugar", True, "gray7")
texto_boton_puntajes = fuente.render("Puntajes", True, "gray7")
texto_boton_salir = fuente.render("Salir", True, "gray7")


# Rectangulos (Rects)
rect_texto_inicio = texto_pantalla_inicio.get_rect()
rect_texto_inicio.x = (pantalla.get_width() - rect_texto_inicio.width) / 2
rect_puntajes = texto_pantalla_puntajes.get_rect()
rect_puntajes.x = (pantalla.get_width() - rect_puntajes.width) / 2


# Botones
boton_ir_puntajes_ancho = pantalla.get_width() * 0.2
boton_ir_puntajes_alto = pantalla.get_height() * 0.1
boton_ir_puntajes_x = (pantalla.get_width() - boton_ir_puntajes_ancho) / 2
boton_ir_puntajes_y = pantalla.get_height() * 0.50
rect_boton_ir_puntajes = pygame.Rect(boton_ir_puntajes_x, boton_ir_puntajes_y, boton_ir_puntajes_ancho, boton_ir_puntajes_alto)

boton_volver_inicio_ancho = pantalla.get_width() * 0.1
boton_volver_inicio_alto = pantalla.get_height() * 0.1
boton_volver_inicio_x = pantalla.get_width() * 0.02
boton_volver_inicio_y = pantalla.get_height() * 0.02
rect_volver_inicio = pygame.Rect(boton_volver_inicio_x, boton_volver_inicio_y, boton_volver_inicio_ancho, boton_volver_inicio_alto)

boton_salir_ancho = pantalla.get_width() * 0.2
boton_salir_alto = pantalla.get_height() * 0.1
boton_salir_x = (pantalla.get_width() - boton_salir_ancho) / 2
boton_salir_y = pantalla.get_height() * 0.68
rect_boton_salir = pygame.Rect(boton_salir_x, boton_salir_y, boton_salir_ancho, boton_salir_alto)

boton_jugar_ancho = pantalla.get_width() * 0.2
boton_jugar_alto = pantalla.get_height() * 0.1
boton_jugar_x = (pantalla.get_width() - boton_jugar_ancho) / 2
boton_jugar_y = pantalla.get_height() * 0.32
rect_boton_jugar = pygame.Rect(boton_jugar_x, boton_jugar_y, boton_jugar_ancho, boton_jugar_alto)

caja_texto_ancho = pantalla.get_width() * 0.7
caja_texto_alto = pantalla.get_height() * 0.2
caja_texto_x = (pantalla.get_width() - caja_texto_ancho) / 2
caja_texto_y = (pantalla.get_height() - caja_texto_alto) / 2
caja_texto = pygame.Rect(caja_texto_x, caja_texto_y, caja_texto_ancho, caja_texto_alto)

imagen_flecha_volver_escalada = pygame.transform.scale(imagen_flecha_volver, (rect_volver_inicio.width * 0.75, rect_volver_inicio.height * 0.75))
rect_flecha_volver = imagen_flecha_volver_escalada.get_rect()
rect_flecha_volver.x = ((rect_volver_inicio.width - rect_flecha_volver.width) / 2) + rect_volver_inicio.x
rect_flecha_volver.y = ((rect_volver_inicio.height - rect_flecha_volver.height) / 2) + rect_volver_inicio.y

texto_boton_jugar = pygame.transform.scale(texto_boton_jugar, (rect_boton_jugar.width * 0.8, rect_boton_jugar.height * 0.8))
rect_texto_jugar = texto_boton_jugar.get_rect()
rect_texto_jugar.x = ((rect_boton_jugar.width - rect_texto_jugar.width) / 2) + rect_boton_jugar.x
rect_texto_jugar.y = ((rect_boton_jugar.height - rect_texto_jugar.height) / 2) + rect_boton_jugar.y

texto_boton_puntajes = pygame.transform.scale(texto_boton_puntajes, (rect_boton_ir_puntajes.width * 0.8, rect_boton_ir_puntajes.height * 0.8))
rect_texto_puntajes = texto_boton_puntajes.get_rect()
rect_texto_puntajes.x = ((rect_boton_ir_puntajes.width - rect_texto_puntajes.width) / 2) + rect_boton_ir_puntajes.x
rect_texto_puntajes.y = ((rect_boton_ir_puntajes.height - rect_texto_puntajes.height) / 2) + rect_boton_ir_puntajes.y

texto_boton_salir = pygame.transform.scale(texto_boton_salir, (rect_boton_salir.width * 0.8, rect_boton_salir.height * 0.8))
rect_texto_salir = texto_boton_salir.get_rect()
rect_texto_salir.x = ((rect_boton_salir.width - rect_texto_salir.width) / 2) + rect_boton_salir.x
rect_texto_salir.y = ((rect_boton_salir.height - rect_texto_salir.height) / 2) + rect_boton_salir.y

# margen_x = pantalla.get_width() * 0.02
margen_y = pantalla.get_height() * 0.02
alto_rc = pantalla.get_height() - (margen_y * 2)
margen_x = pantalla.get_width() - alto_rc - (pantalla.get_width() * 0.02)
rectangulo_contenedor = pygame.Rect(margen_x, margen_y, alto_rc, alto_rc)
generar_rectangulos(matriz, rectangulo_contenedor)

corriendo = True
nombre_usuario = ""
texto_nombre_usuario = fuente.render(nombre_usuario, True, "black")

caja_texto_activada = False
pantalla_actual = "Inicio" # Bool, String, Int

while corriendo == True:
    # Pantalla Inicio
    if pantalla_actual == "Inicio":
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_boton_ir_puntajes.collidepoint(evento.pos) == True:
                    pantalla_actual = "Puntajes"
                if rect_boton_salir.collidepoint(evento.pos) == True:
                    corriendo = False
                if rect_boton_jugar.collidepoint(evento.pos) == True:
                    pantalla_actual = "Juego"

        pantalla.fill("gold3")
        pantalla.blit(texto_pantalla_inicio, rect_texto_inicio) # Encabezado
        pygame.draw.rect(pantalla, "darkorchid", rect_boton_jugar, border_radius=15)
        pantalla.blit(texto_boton_jugar, rect_texto_jugar)
        pygame.draw.rect(pantalla, "darkorchid", rect_boton_ir_puntajes, border_radius=15)
        pantalla.blit(texto_boton_puntajes, rect_texto_puntajes)
        pygame.draw.rect(pantalla, "darkorchid", rect_boton_salir, border_radius=15)
        pantalla.blit(texto_boton_salir, rect_texto_salir)


    # Pantalla Puntajes
    elif pantalla_actual == "Puntajes":
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_volver_inicio.collidepoint(evento.pos) == True:
                    pantalla_actual = "Inicio"
                if caja_texto.collidepoint(evento.pos) == True:
                    caja_texto_activada = True
                    nombre_usuario = ""
            if evento.type == pygame.KEYDOWN and caja_texto_activada == True:
                if evento.key == pygame.K_BACKSPACE:
                    nombre_usuario = nombre_usuario[:-1]
                elif evento.key == pygame.K_RETURN:
                    caja_texto_activada = False
                else:
                    if len(nombre_usuario) < 9: 
                        nombre_usuario += evento.unicode


        pantalla.fill("darkgoldenrod")
        pantalla.blit(texto_pantalla_puntajes, rect_puntajes)
        pygame.draw.rect(pantalla, "darkorchid", rect_volver_inicio, border_radius=50)
        pantalla.blit(imagen_flecha_volver_escalada, rect_flecha_volver)
        if caja_texto_activada == False:
            pygame.draw.rect(pantalla, "black", caja_texto, border_radius=15, width=25)
        else:
            pygame.draw.rect(pantalla, (4, 113, 201), caja_texto, border_radius=15, width=25)
    
        texto_nombre_usuario = fuente.render(nombre_usuario, True, "black")
        ubicacion_texto_x = ((caja_texto.width - texto_nombre_usuario.get_width()) / 2) + caja_texto.x
        ubicacion_texto_y = ((caja_texto.height - texto_nombre_usuario.get_height()) / 2) + caja_texto.y
        pantalla.blit(texto_nombre_usuario, (ubicacion_texto_x, ubicacion_texto_y))

    elif pantalla_actual == "Juego":
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(matriz)):
                    for j in range(len(matriz[i])):
                        if matriz[i][j]["rect"].collidepoint(evento.pos) == True:
                            print(f"Apretaste sobre celda {i} - {j}")
                            matriz[i][j]["color"] = "black"
        
        pantalla.fill((255, 255, 255)) # Fondo de pantalla blanco
        pygame.draw.rect(pantalla, "black", rectangulo_contenedor)
        dibujar_matriz(matriz, pantalla)

    pygame.display.flip() 


# Falta: hacer una matriz de botones (diccionarios), implementar el textbox.


# Colecciones y sus metodos y caracteristicas (listas, sets, tuplas y diccionarios).
# Archivos.