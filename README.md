# 💎 Juego Match-3

**Juego Match-3** es un videojuego 2D desarrollado en **Python** utilizando la biblioteca **Pygame**, implementando la mecánica clásica del género *match-3*, donde el jugador debe intercambiar fichas en una grilla para formar combinaciones de tres o más elementos iguales.

El proyecto fue realizado como trabajo académico universitario con el objetivo de aplicar conceptos fundamentales de programación estructurada y orientada a objetos en el desarrollo de videojuegos.

---

# 🎮 Gameplay

El juego consiste en una grilla de fichas donde el jugador puede intercambiar posiciones entre piezas adyacentes para formar combinaciones.

Cuando se genera una combinación válida:

* las fichas coincidentes se eliminan
* se actualiza la grilla
* nuevas fichas aparecen automáticamente
* el tablero se reorganiza dinámicamente

El objetivo principal es generar la mayor cantidad de combinaciones posibles.

El juego pertenece al género:

```
Puzzle / Match-3
```

Inspirado en títulos como:

```
Candy Crush
Bejeweled
```

---

# 🧠 Objetivos académicos del proyecto

Este proyecto fue desarrollado para aplicar conceptos clave de programación de videojuegos en Python:

* manejo de estructuras matriciales
* detección de patrones en grillas
* control de eventos del mouse
* renderizado en tiempo real con Pygame
* actualización dinámica del tablero
* lógica de eliminación y reposición de fichas
* separación modular de responsabilidades
* control del game loop

---

# ⚙️ Tecnologías utilizadas

Lenguaje:

```
Python
```

Biblioteca gráfica:

```
Pygame
```

Control de versiones:

```
Git
GitHub
```

IDE compatible:

```
VSCode
PyCharm
```

---

# 🏗️ Arquitectura del proyecto

El proyecto implementa una estructura modular basada en el manejo de tablero y lógica de combinaciones.

Componentes principales:

### Game Loop

Responsable de:

* actualización del estado del juego
* renderizado de la grilla
* procesamiento de input del usuario
* control de eventos

Permite mantener interacción en tiempo real con el tablero.

---

### Sistema de grilla

El tablero está representado mediante:

```
estructura matricial bidimensional
```

Esta estructura permite:

* almacenar fichas
* detectar coincidencias
* validar intercambios
* actualizar posiciones
* reorganizar elementos tras eliminaciones

---

### Sistema de selección e intercambio

El jugador puede:

* seleccionar fichas con el mouse
* intercambiar fichas adyacentes
* validar si el movimiento genera coincidencias

Solo los movimientos válidos generan cambios permanentes.

---

### Detección de combinaciones

El juego implementa detección automática de:

```
3 o más fichas iguales consecutivas
```

En:

* filas
* columnas

Cuando se detecta coincidencia:

* se eliminan las fichas
* se actualiza el tablero
* se generan nuevas piezas

---

### Sistema de reposición de fichas

Luego de eliminar combinaciones:

* las fichas superiores descienden
* se generan nuevas fichas aleatorias
* el tablero se recompone automáticamente

Esto mantiene continuidad en el gameplay.

---

# 🔁 Game Loop

El juego utiliza el loop principal de Pygame para controlar:

* actualización visual
* lógica del tablero
* detección de eventos
* interacción del usuario

Esto garantiza fluidez durante la partida.

---

# 🖱️ Sistema de input

El input del jugador se realiza mediante:

```
mouse
```

Permite:

* seleccionar fichas
* intercambiar posiciones
* interactuar con la grilla

---

# 📁 Estructura del proyecto

Estructura general:

```
juego_match-3/
 ├── main.py
 ├── board.py
 ├── tile.py
 ├── settings.py
 └── assets/
```

Separación clara entre:

* lógica del juego
* representación del tablero
* configuración
* recursos gráficos

---

# 🚀 Cómo ejecutar el proyecto

1. Clonar el repositorio:

```
git clone https://github.com/ManuelMagide/juego_match-3.git
```

2. Instalar dependencias:

```
pip install pygame
```

3. Ejecutar el juego:

```
python main.py
```

---

# 🎯 Funcionalidades implementadas

Actualmente el juego incluye:

✔ tablero dinámico
✔ selección de fichas con mouse
✔ intercambio de piezas adyacentes
✔ detección automática de combinaciones
✔ eliminación de fichas coincidentes
✔ reposición automática de piezas
✔ actualización visual en tiempo real
✔ lógica completa del género match-3

---

# 🔮 Posibles mejoras futuras

El proyecto puede ampliarse con:

* sistema de puntuación
* contador de movimientos
* niveles con objetivos
* efectos visuales
* animaciones de transición
* sonidos
* temporizador de partida
* piezas especiales
* combos encadenados

---

# 👨‍💻 Autor

**Manuel Magide**

Proyecto desarrollado como trabajo práctico universitario.

Repositorio:

```
https://github.com/ManuelMagide/juego_match-3.git
```

---

# 📄 Licencia

Proyecto desarrollado con fines educativos.
Uso permitido como material de aprendizaje.
