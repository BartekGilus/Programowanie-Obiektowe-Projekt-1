import pygame, os
from tkinter import *
from tkinter import messagebox
from settings import *
from Player import *
from Level import *

class Game():

    def __init__(self):
        self.RUNNING = True
        self.play_again = False
        pygame.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.window = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('Przeszukiwanie Labiryntu')
        self.clock = pygame.time.Clock()
        self.play_again = None

        self.init()

    def collision_detection(self):
        colliding_solid = pygame.sprite.spritecollide(self.player, self.level.set_of_solid_plates, False)
        colliding_road = pygame.sprite.spritecollide(self.player, self.level.set_of_road_plates, False)

        for plate in colliding_solid:
            if self.player.direction == 'UP':
                self.player.rect.top = plate.rect.bottom
            if self.player.direction == 'DOWN':
                self.player.rect.bottom = plate.rect.top
            if self.player.direction == 'LEFT':
                self.player.rect.left = plate.rect.right
            if self.player.direction == 'RIGHT':
                self.player.rect.right = plate.rect.left

        for plate in colliding_road:
            plate.visited = True

    def possible_ways(self):
        self.East = False
        self.South = False
        self.West = False
        self.North = False
        for x in self.level.set_of_road_plates:
            if self.player.rect.right == x.rect.right and self.player.rect.bottom == x.rect.bottom and x.finish:
                self.play_again = self.win_message()
            else:
                if self.player.rect.right == x.rect.left and self.player.rect.bottom == x.rect.bottom and not x.visited:
                    self.East = True
                if self.player.rect.bottom == x.rect.top and self.player.rect.right == x.rect.right and not x.visited:
                    self.South = True
                if self.player.rect.left == x.rect.right and self.player.rect.bottom == x.rect.bottom and not x.visited:
                    self.West = True
                if self.player.rect.top == x.rect.bottom and self.player.rect.right == x.rect.right and not x.visited:
                    self.North = True

    def uncover(self):
        for x in self.level.set_of_cover_plates:
            if self.player.rect.top == x.rect.bottom and self.player.rect.right == x.rect.right:
                x.image = BLANK_S
            elif self.player.rect.top == x.rect.bottom and self.player.rect.x + 48 == x.rect.x:
                x.image = BLANK_S
            elif self.player.rect.top == x.rect.bottom and self.player.rect.x - 48 == x.rect.x:
                x.image = BLANK_S
            elif self.player.rect.bottom == x.rect.top and self.player.rect.right == x.rect.right:
                x.image = BLANK_S
            elif self.player.rect.bottom == x.rect.top and self.player.rect.x + 48 == x.rect.x:
                x.image = BLANK_S
            elif self.player.rect.bottom == x.rect.top and self.player.rect.x - 48 == x.rect.x:
                x.image = BLANK_S
            elif self.player.rect.right == x.rect.left and self.player.rect.bottom == x.rect.bottom:
                x.image = BLANK_S
            elif self.player.rect.left == x.rect.right and self.player.rect.bottom == x.rect.bottom:
                x.image = BLANK_S
            elif self.player.rect.right == x.rect.right and self.player.rect.bottom == x.rect.bottom:
                x.image = BLANK_S
            else:
                x.image = BLACK_S

    def game_rules(self, event):
        self.possible_ways()
        if self.East:
            if event.type == pygame.KEYDOWN:
                if event.key != pygame.K_RIGHT:
                    self.RUNNING = False
                    self.play_again = self.game_over_message()
        else:
            if self.South:
                if event.type == pygame.KEYDOWN:
                    if event.key != pygame.K_DOWN:
                        self.RUNNING = False
                        self.play_again = self.game_over_message()
            else:
                if self.West:
                    if event.type == pygame.KEYDOWN:
                        if event.key != pygame.K_LEFT:
                            self.RUNNING = False
                            self.play_again = self.game_over_message()

    def game_over_message(self):
        Tk().wm_withdraw()
        return messagebox.askyesno("Nieprawidłowy ruch!", "Nieprawidłowy ruch jeżeli chcesz zagrac jeszcze raz nacisnij Tak.")

    def win_message(self):
        Tk().wm_withdraw()
        return messagebox.askyesno("BRAWO!", "Udało Ci sie pokonać labirynt, jeżeli chcesz zagrac jeszcze raz naciśnij Tak.")

    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.RUNNING = False
        elif event.type == pygame.KEYUP:
            pass
        elif event.type == pygame.QUIT:
            self.RUNNING = False

    def init(self):
        self.level = Level()
        self.player = Player(PLAYER_S, self.level.start_x, self.level.start_y)

    def update(self):
        self.player.update()
        self.collision_detection()
        self.uncover()

    def draw(self, surface):
        self.level.draw(surface)
        self.player.draw(surface)
        self.level.draw_cover(surface)

    def reset(self):
        self.__init__()

    def run(self):

        while self.RUNNING:
            self.window.blit(BACKGROUND_I, (0, 0))

            for event in pygame.event.get():
                self.event_handler(event)
                self.player.event_handler(event)
                self.game_rules(event)

            if self.play_again:
                self.reset()


            self.update()
            self.draw(self.window)
            pygame.display.flip()
            self.clock.tick(30)

pygame.quit()