import pygame
from pygame import mixer
from game import Game

# Inicializamos Pygame
pygame.init()

# Creamos la ventana
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bug Buster")
ICON_IMG = 'images/ufo.png'
icon = pygame.image.load(ICON_IMG)
pygame.display.set_icon(icon)
mixer.music.load("sounds/menu.wav")
mixer.music.play(-1)

# Fuente para mostrar el texto
font = pygame.font.Font('freesansbold.ttf', 32)

def draw_text(text, x, y):
    label = font.render(text, True, (255, 255, 255))
    screen.blit(label, (x, y))

def main_menu():
    menu_running = True
    while menu_running:
        screen.fill((0, 0, 0))
        
        # Mostrar opciones de dificultad
        draw_text("Selecciona la Dificultad", 200, 100)
        draw_text("1. Fácil", 200, 200)
        draw_text("2. Normal", 200, 300)
        draw_text("3. Difícil", 200, 400)

        pygame.display.update()

        # Revisar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    menu_running = False
                    game = Game('images/background1.jpg', 'images/enemy1.png', 0.3, 40, 4)  # Fácil
                    game.run()
                if event.key == pygame.K_2:
                    menu_running = False
                    game = Game('images/background2.jpg', 'images/enemy2.png', 0.5, 50, 6)  # Normal
                    game.run()
                if event.key == pygame.K_3:
                    menu_running = False
                    game = Game('images/background3.jpg', 'images/enemy3.png', 0.7, 60, 8)  # Difícil
                    game.run()

# Ejecutar menú principal
main_menu()
