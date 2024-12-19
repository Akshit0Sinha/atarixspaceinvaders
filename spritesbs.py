
import pygame as pg
from mainbs import *
from pygame.sprite import Sprite
from settingbs import *
from mainbs import *

vec = pg.math.Vector2

#paddle code
class Paddle(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.all_paddles
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((TILESIZE*3,TILESIZE/2))
        self.rect = self.image.get_rect()
        self.image.fill(RED)
        self.x = x * TILESIZE 
        self.y = y * TILESIZE
        self.speed = 10
        self.vx, self.vy = 0, 0
        print("i Created a paddle...")
# code to move paddle
    def get_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vx -= self.speed
        if keys[pg.K_RIGHT]:
            self.vx += self.speed

            
# paddle colliding with ball
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
            if hits:
                if self.vx > 0:
                    #self.x = hits[0].rect.left + TILESIZE
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        #y dir for collision of wall w paddle
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
        
        #collide with paddle and powerup
    def collide_with_stuff(self, group, kill):
        hits = pg.sprite.spritecollide(self, group, kill)
        if hits:
            if str(hits[0].__class__.__name__) == "Powerup":
                print("i hit a powerup...")
                self.speed =+ 5
    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        # reverse order to fix collision issues
        
        self.rect.x = self.x
        self.collide_with_walls('x')
        
        self.rect.y = self.y
        self.collide_with_walls('y')
        

#projectile is ball, so initializing ball
class Projectile(Sprite):
    def __init__(self, game, x, y,):
        self.game = game
        self.groups = game.all_sprites, game.all_projectiles
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((TILESIZE/2, TILESIZE/2))
        self.rect = self.image.get_rect()
        self.image.fill(GREEN)
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.vx = 5 
        self.vy = 5
        self.speed = 1
        #physics on ball with colliding, movement, etc
    def update(self):
        self.rect.y -= self.speed
        #projectile_radius = 20
        #projectile_x = WIDTH // 2
        #projectile_y = HEIGHT // 2
        projectile_dx = 5  
        projectile_dy = 5  
         #self.vx += self.x
         #self.vy += self.dy
        #if projectile_x - projectile_radius <= 0 or projectile_x + projectile_radius >= WIDTH:
           #projectile_dx = -3/2*projectile_dy
        #if projectile_y - projectile_radius <= 0 or projectile_y + projectile_radius >= HEIGHT:
            #projectile_dy = 3/2* projectile_dx

 # collide ball with blocks
        self.rect.x += self.vx * self.speed *-1
        self.rect.y += self.vy * self.speed *-1
        hits = pg.sprite.spritecollide(self, self.game.all_blocks, True)
        whits = pg.sprite.spritecollide(self, self.game.all_walls, False)#
        phits = pg.sprite.collide_rect(self, self.game.player)
        lhits = pg.sprite.spritecollide(self,self.game.all_lava, True)
        if hits:
            print("I hit a block")
            self.speed *= -1
            self.vx = self.vx
            self.vy = -self.vy
        if whits:
            print("I hit a wall")
            if self.rect.right > WIDTH:
                print("I Hit the right wall")
                self.vx = -self.vx
                self.vy = self.vy
            elif self.rect.left < 0:
                print("I hit the left wall!")
                self.vy = self.vy
                self.vx = -self.vx
            elif self.rect.top < 0:
                print("I hit the roof")
                self.vy = -self.vy
                self.vx = self.vx
            #self.rect.x = self.vx
            #self.rect.y = self.vy
        if phits:
            print("I hit a paddle")
            self.speed *= -1
            self.vx = -self.vy
            self.vy = -self.vx
        if lhits:
            print("I hit lava")
            pg.quit
    
        
#blocks on screen
class Block(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.all_blocks
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(BLUE)
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.x = x
        self.y = y
        self.visible = True  # To track if the block is still active 
    
    # def update(self):
    #     """Update game state: move the ball and check for collisions."""
    #     game.projectile_update()  # Move the ball
    #     self.check_collisions()  # Check for collisions with blocks
        
#wall on three sides 
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

class Lava(Sprite):
    def __init__(self,game,x,y):
        self.game = game
        self.groups = game.all_sprites, game.all_lava
        Sprite.__init__(self,self.groups)
        self.image = pg.Surface((TILESIZE,TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(LAVA)
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
