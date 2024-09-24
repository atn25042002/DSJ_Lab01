import pygame
import math
import random
from pygame import mixer

class Game:
    def __init__(self, background_img, enemy_img, enemy_speed_x, enemy_speed_y, num_of_enemies):
        # Initialize pygame
        pygame.init()

        # Global Variables for Game Settings
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.PLAYER_START_X = 370
        self.PLAYER_START_Y = 480
        self.PLAYER_SPEED = 0.5
        self.BULLET_SPEED = 2
        self.COLLISION_DISTANCE = 27

        # Music and Sounds
        self.BACKGROUND_MUSIC = 'sounds/background.wav'
        self.BULLET_SOUND = 'sounds/laser.wav'
        self.EXPLOSION_SOUND = 'sounds/explosion.wav'

        # Sprites
        self.BACKGROUND_IMG = background_img
        self.PLAYER_IMG = 'images/player.png'
        self.BULLET_IMG = 'images/bullet.png'
        self.ICON_IMG = 'images/ufo.png'
        self.ENEMY_IMG = enemy_img

        # Create the screen
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # Load Background
        self.background = pygame.image.load(self.BACKGROUND_IMG)

        # Load Sounds
        mixer.music.load(self.BACKGROUND_MUSIC)
        mixer.music.play(-1)

        # Title and Icon
        pygame.display.set_caption("Bug Buster")
        icon = pygame.image.load(self.ICON_IMG)
        pygame.display.set_icon(icon)

        # Player Variables
        self.playerImg = pygame.image.load(self.PLAYER_IMG)
        self.playerX = self.PLAYER_START_X
        self.playerY = self.PLAYER_START_Y
        self.playerX_change = 0

        # Enemy Variables (set by the difficulty parameters)
        self.enemyImg = []
        self.enemyX = []
        self.enemyY = []
        self.enemyX_change = []
        self.enemyY_change = []

        for i in range(num_of_enemies):
            self.enemyImg.append(pygame.image.load(self.ENEMY_IMG))
            self.enemyX.append(random.randint(0, self.SCREEN_WIDTH - 64))
            self.enemyY.append(random.randint(50, 150))
            self.enemyX_change.append(enemy_speed_x)
            self.enemyY_change.append(enemy_speed_y)

        # Bullet Variables
        self.bulletImg = pygame.image.load(self.BULLET_IMG)
        self.bulletX = 0
        self.bulletY = self.PLAYER_START_Y
        self.bulletX_change = 0
        self.bulletY_change = self.BULLET_SPEED
        self.bullet_state = "ready"

        # Score
        self.score_value = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.textX = 10
        self.textY = 10

        # Game Over text
        self.over_font = pygame.font.Font('freesansbold.ttf', 64)

    def show_score(self):
        score = self.font.render("Score :" + str(self.score_value), True, (0, 255, 0))
        self.screen.blit(score, (self.textX, self.textY))

    def game_over_text(self):
        over_text = self.over_font.render("GAME OVER", True, (0, 255, 0))
        self.screen.blit(over_text, (200, 250))

    def player(self):
        self.screen.blit(self.playerImg, (self.playerX, self.playerY))

    def enemy(self, i):
        self.screen.blit(self.enemyImg[i], (self.enemyX[i], self.enemyY[i]))

    def fire_bullet(self):
        self.bullet_state = "fire"
        self.screen.blit(self.bulletImg, (self.bulletX + 16, self.bulletY + 10))

    def isCollision(self, enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
        return distance < self.COLLISION_DISTANCE

    def show_pause_menu(self):
        pause_font = pygame.font.Font(None, 74)
        pause_text = pause_font.render("Paused", True, (255, 255, 255))
        continue_text = self.font.render("Press C to Continue", True, (255, 255, 255))
        quit_text = self.font.render("Press Q to Quit", True, (255, 255, 255))

        self.screen.fill((0, 0, 0))
        self.screen.blit(pause_text, (self.SCREEN_WIDTH // 2 - 100, self.SCREEN_HEIGHT // 2 - 100))
        self.screen.blit(continue_text, (self.SCREEN_WIDTH // 2 - 150, self.SCREEN_HEIGHT // 2))
        self.screen.blit(quit_text, (self.SCREEN_WIDTH // 2 - 150, self.SCREEN_HEIGHT // 2 + 50))

        pygame.display.update()

        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:  # Continuar
                        paused = False
                    if event.key == pygame.K_q:  # Salir al menú de niveles
                        return True  # Vuelve al menú principal

        return False
    
    def run(self):
        # Main game loop
        running = True
        while running:
            # RGB color fill
            self.screen.fill((0, 0, 0))

            # Background image
            self.screen.blit(self.background, (0, 0))

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Keyboard input
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.playerX_change = -self.PLAYER_SPEED
                    if event.key == pygame.K_RIGHT:
                        self.playerX_change = self.PLAYER_SPEED
                    if event.key == pygame.K_SPACE:
                        if self.bullet_state == "ready":
                            self.bulletX = self.playerX
                            self.fire_bullet()
                            mixer.Sound(self.BULLET_SOUND).play()
                    if event.key == pygame.K_p:  # Pausa el juego con la tecla 'P'
                        if self.show_pause_menu():  # Retorna True si se selecciona salir
                            return

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.playerX_change = 0

            # Player movement
            self.playerX += self.playerX_change
            if self.playerX <= 0:
                self.playerX = 0
            elif self.playerX >= self.SCREEN_WIDTH - 64:
                self.playerX = self.SCREEN_WIDTH - 64

            # Enemy movement
            for i in range(len(self.enemyX)):
                # Game Over condition
                if self.enemyY[i] > 440:
                    for j in range(len(self.enemyX)):
                        self.enemyY[j] = 2000
                    self.game_over_text()
                    break

                self.enemyX[i] += self.enemyX_change[i]
                if self.enemyX[i] <= 0:
                    self.enemyX_change[i] = abs(self.enemyX_change[i])
                    self.enemyY[i] += self.enemyY_change[i]
                elif self.enemyX[i] >= self.SCREEN_WIDTH - 64:
                    self.enemyX_change[i] = -abs(self.enemyX_change[i])
                    self.enemyY[i] += self.enemyY_change[i]

                # Collision check
                collision = self.isCollision(self.enemyX[i], self.enemyY[i], self.bulletX, self.bulletY)
                if collision:
                    self.bulletY = self.PLAYER_START_Y
                    self.bullet_state = "ready"
                    self.score_value += 1
                    mixer.Sound(self.EXPLOSION_SOUND).play()
                    self.enemyX[i] = random.randint(0, self.SCREEN_WIDTH - 64)
                    self.enemyY[i] = random.randint(50, 150)

                self.enemy(i)

            # Bullet movement
            if self.bulletY <= 0:
                self.bulletY = self.PLAYER_START_Y
                self.bullet_state = "ready"

            if self.bullet_state == "fire":
                self.fire_bullet()
                self.bulletY -= self.bulletY_change

            # Render player and score
            self.player()
            self.show_score()

            # Update display
            pygame.display.update()
