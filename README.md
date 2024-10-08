# Exterminador de Insectos Mutantes

## Descripción
"Exterminador de Insectos Mutantes" es un emocionante juego de acción desarrollado en Python utilizando la biblioteca Pygame. En este juego, los jugadores controlan una nave espacial con la misión de exterminar insectos mutantes que amenazan la galaxia. El juego ofrece múltiples niveles de dificultad y una interfaz de pausa para una experiencia de juego completa.

## Estructura del Proyecto

```
exterminador_insectos/
├── game.py           # Código principal del juego
├── main.py           # Archivo que inicia el juego y gestiona el menú
├── requirements.txt  # Dependencias del proyecto
├── .gitignore        # Archivos y directorios ignorados por Git
├── sounds/           # Carpeta que contiene los archivos de sonido del juego
│   ├── background.wav  # Música de fondo
│   ├── explosion.wav   # Sonido de explosión
│   └── laser.wav       # Sonido del disparo
└── images/           # Carpeta que contiene los sprites y fondos del juego
    ├── background.jpg  # Imagen de fondo
    ├── enemy.png       # Sprite del enemigo
    ├── player.png      # Sprite del jugador
    └── bullet.png      # Sprite de la bala
```

## Requisitos
- Python 3.x
- Pygame

## Instalación

1. **Clona el repositorio**:
   ```sh
   git clone <URL_DEL_REPOSITORIO>
   cd exterminador_insectos
   ```

2. **Crea un entorno virtual**:
   ```sh
   python -m venv venv
   ```

3. **Activa el entorno virtual**:
   - En Windows:
     ```sh
     .\venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

4. **Instala las dependencias**:
   ```sh
   pip install -r requirements.txt
   ```

## Ejecución del Juego

Una vez que hayas configurado el entorno virtual y hayas instalado las dependencias, puedes ejecutar el juego con el siguiente comando:

```sh
python main.py
```

## Controles
- **Flecha izquierda**: Mover la nave a la izquierda
- **Flecha derecha**: Mover la nave a la derecha
- **Barra espaciadora**: Disparar
- **P**: Pausar/Reanudar el juego
- **ESC**: Salir al menú principal

## Características
- Múltiples niveles de dificultad
- Sistema de puntuación
- Efectos de sonido y música de fondo
- Menú principal y pantalla de pausa

## Créditos
Desarrollado por Anthony Edwin Aco Tito