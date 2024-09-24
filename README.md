# Exterminador de Insectos Mutantes

## Descripción
Este es un juego desarrollado en Python usando Pygame, donde el jugador controla una nave que debe exterminar insectos mutantes. El juego cuenta con varios niveles de dificultad y una interfaz de pausa.

## Estructura del Proyecto

exterminador_insectos/ ├── game.py # Código principal del juego ├── main.py # Archivo que inicia el juego y gestiona el menú ├── requirements.txt # Dependencias del proyecto ├── .gitignore # Archivos y directorios ignorados por Git ├── sounds/ # Carpeta que contiene los archivos de sonido del juego │ ├── background.wav # Música de fondo │ ├── explosion.wav # Sonido de explosión │ └── laser.wav # Sonido del disparo └── images/ # Carpeta que contiene los sprites y fondos del juego ├── background.jpg # Imagen de fondo ├── enemy.png # Sprite del enemigo ├── player.png # Sprite del jugador └── bullet.png # Sprite de la bala

markdown
Copiar código

## Requisitos
- Python 3.x
- Pygame

## Instalación

1. **Clona el repositorio**:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd exterminador_insectos
Crea un entorno virtual:

bash
Copiar código
python -m venv venv
Activa el entorno virtual:

En Windows:
bash
Copiar código
.\venv\Scripts\activate
En macOS/Linux:
bash
Copiar código
source venv/bin/activate
Instala las dependencias:

bash
Copiar código
pip install -r requirements.txt
Ejecución del Juego
Una vez que hayas configurado el entorno virtual y hayas instalado las dependencias, puedes ejecutar el juego con el siguiente comando:

bash
Copiar código
python main.py
Controles
Flecha izquierda: Mover la nave a la izquierda
Flecha derecha: Mover la nave a la derecha
Barra espaciadora: Disparar
Créditos
Desarrollado por [Tu Nombre] (opcional)