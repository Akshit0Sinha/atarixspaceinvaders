import pygame as pg
from pygame.sprite import Sprite
from settingbs import *

class paddle(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites  
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((32,32))
        self.rect = self.image.get_rect()
        self.image.fill(RED)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 10
        self.vx, self.vy = 0, 0

    def get_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vy -= self.speed
        if keys[pg.K_RIGHT]:
            self.vx -= self.speed
       