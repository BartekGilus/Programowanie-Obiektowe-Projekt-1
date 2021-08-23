import pygame

class Plate(pygame.sprite.Sprite):

    def __init__(self, image, pos_x, pos_y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Solid_Plate(Plate):

    def __init__(self, image, pos_x, pos_y):
        super().__init__(image, pos_x, pos_y)
        self.is_solid = True


class Road_Plate(Plate):

    def __init__(self, image, pos_x, pos_y):
        super().__init__(image, pos_x, pos_y)
        self.is_solid = False
        self.visited = False
        self.finish = False
        self.start = False

class Cover_Plate(Plate):

    def __init__(self, image, pos_x, pos_y):
        super().__init__(image, pos_x, pos_y)
        self.is_solid = False