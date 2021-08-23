import pygame, os

# Utawienia okna gry
SCREEN_SIZE = WIDTH, HEIGHT = 1366, 768

# Sprites
BACKGROUND_I = pygame.image.load(os.path.join('img', 'maze.png'))
BLACK_S = pygame.image.load(os.path.join('img', 'black.png'))
YELLOW_S = pygame.image.load(os.path.join('img', 'yellow.png'))
ROCK_S = pygame.image.load(os.path.join('img', 'rock.png'))
BLANK_S = pygame.image.load(os.path.join('img', 'blank.png'))
PLAYER_U = pygame.image.load(os.path.join('img', 'player_2.png'))
PLAYER_D = pygame.image.load(os.path.join('img', 'player_4.png'))
PLAYER_L = pygame.image.load(os.path.join('img', 'player_1.png'))
PLAYER_R = pygame.image.load(os.path.join('img', 'player_3.png'))

PLAYER_S = [PLAYER_U, PLAYER_D, PLAYER_L, PLAYER_R]