import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, images, pos_x, pos_y):
        super().__init__()
        self.images = images
        self.image = images[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speed = 48
        self.flag = True
        self.direction = None
        self.starting_image()

    def update(self):
        if self.direction == 'UP':
            if self.flag:
                self.rect.y -= self.speed
                self.image = self.images[0]
                self.flag = False
        elif self.direction == 'DOWN':
            if self.flag:
                self.rect.y += self.speed
                self.image = self.images[1]
                self.flag = False
        elif self.direction == 'LEFT':
            if self.flag:
                self.rect.x -= self.speed
                self.image = self.images[2]
                self.flag = False
        elif self.direction == 'RIGHT':
            if self.flag:
                self.rect.x += self.speed
                self.image = self.images[3]
                self.flag = False

    def starting_image(self):
        if self.rect.x == 240 + 48:
            self.image = self.images[3]
        elif self.rect.y == 144 + 48:
            self.image = self.images[1]
        elif self.rect.x == 1152 - 48:
            self.image = self.images[2]
        elif self.rect.y == 528 - 48:
            self.image = self.images[0]

    def stop(self):
        self.direction = None
        self.flag = True

    def event_handler(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                self.direction = 'UP'
                self.image = self.images[0]
            elif e.key == pygame.K_DOWN:
                self.direction = 'DOWN'
                self.image = self.images[1]
            elif e.key == pygame.K_LEFT:
                self.direction = 'LEFT'
                self.image = self.images[2]
            elif e.key == pygame.K_RIGHT:
                self.direction = 'RIGHT'
                self.image = self.images[3]
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_UP:
                self.stop()
            elif e.key == pygame.K_DOWN:
                self.stop()
            elif e.key == pygame.K_LEFT:
                self.stop()
            elif e.key == pygame.K_RIGHT:
                self.stop()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
