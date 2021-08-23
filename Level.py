from Plate import *
from settings import *
from Levels import *
import random

class Level(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.levels = levels
        self.start_x = None
        self.start_y = None
        self.set_of_solid_plates = pygame.sprite.Group()
        self.set_of_road_plates = pygame.sprite.Group()
        self.set_of_cover_plates = pygame.sprite.Group()

        self.cover_level = ["BBBBBBBBBBBBBBBBBBB",
                            "BBBBBBBBBBBBBBBBBBB",
                            "BBBBBBBBBBBBBBBBBBB",
                            "BBBBBBBBBBBBBBBBBBB",
                            "BBBBBBBBBBBBBBBBBBB",
                            "BBBBBBBBBBBBBBBBBBB",
                            "BBBBBBBBBBBBBBBBBBB",
                            "BBBBBBBBBBBBBBBBBBB"]
        self.create_cover()
        self.create_level()

    def create_cover(self):
        self.x = 240
        self.y = 144
        for row in self.cover_level:
            for col in row:
                if col == 'B':
                    p = Cover_Plate(BLACK_S, self.x, self.y)
                    self.set_of_cover_plates.add(p)
                self.x += 48
            self.y += 48
            self.x = 240

    def create_level(self):
        self.x = 240
        self.y = 144
        r = random.randrange(0,3)
        for row in self.levels[r]:
            for col in row:
                if col == 'B':
                    p = Solid_Plate(BLACK_S, self.x, self.y)
                    self.set_of_solid_plates.add(p)
                if col == 'R':
                    p = Road_Plate(YELLOW_S, self.x, self.y)
                    self.set_of_road_plates.add(p)
                if col == 'X':
                    p = Solid_Plate(ROCK_S, self.x, self.y)
                    self.set_of_solid_plates.add(p)
                if col == 'F':
                    p = Road_Plate(YELLOW_S, self.x, self.y)
                    p.finish = True
                    self.set_of_road_plates.add(p)
                if col == 'S':
                    p = Road_Plate(YELLOW_S, self.x, self.y)
                    p.start = True
                    self.start_x = self.x
                    self.start_y = self.y
                    self.set_of_road_plates.add(p)
                self.x += 48
            self.y += 48
            self.x = 240

    def draw_cover(self, surface):
        for y in self.set_of_cover_plates:
            y.draw(surface)

    def draw(self, surface):
        for x in self.set_of_solid_plates:
            x.draw(surface)
        for y in self.set_of_road_plates:
            y.draw(surface)
