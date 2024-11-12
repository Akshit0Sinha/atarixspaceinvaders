import pygame as pg
from mainbs import *
from pygame.sprite import Sprite
from settingbs import *
from mainbs import *

vec = pg.math.Vector2


class paddle(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.all_paddles
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((32,32))
        self.rect = self.image.get_rect()
        self.image.fill(BLUE)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 10
        self.vx, self.vy = 0, 0

    def get_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vx -= self.speed
        if keys[pg.K_RIGHT]:
            self.vx += self.speed
        if pg.mouse.get_pressed()[0]:
            print(pg.mouse.get_pos())
            Projectile(self.game, WIDTH/2, HEIGHT/2)
            print(p.rect.x)
            

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - TILESIZE
                    # self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - TILESIZE
                    # self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y
        
        
        def collide_with_stuff(self, group, kill):
            hits = pg.sprite.spritecollide(self, group, kill)
            if hits:
                if str(hits[0].__class__.__name__) == "Powerup":
                    print("i hit a powerup...")
                    self.speed =+ 5


class Projectile(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.all_projectiles
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(BLUE)
        self.rect.x = x 
        self.rect.y = y 
        
    

class Block(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.all_blocks
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(BLUE)
        self.rect.x = x 
        self.rect.y = y 
    
    def collide_with_stuff(self, group, kill):
            hits = pg.sprite.spritecollide(self, group, kill)
            if hits:
                if str(hits[0].__class__.__name__) == "Projectie":
                    a = "I hit a Block..."
                    print(a))
                    #question about how to delete blocks
                    del a

class Wall(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.all_walls
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(BLUE)
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        
class Powerup(Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.all_powerups
        Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(GREEN)
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def update(self):
        pass


       