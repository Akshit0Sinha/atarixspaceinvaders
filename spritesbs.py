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
        self.image = pg.Surface((32,32))
        self.rect = self.image.get_rect()
        self.image.fill(BLUE)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 10
        self.vx, self.vy = 0, 0
# code to move paddle
    def get_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vx -= self.speed
        if keys[pg.K_RIGHT]:
            self.vx += self.speed
        if pg.mouse.get_pressed()[0]:
            print(pg.mouse.get_pos())
            Projectile(self.game, WIDTH/2, HEIGHT/2)
            print(pg.rect.x)
            
# paddle colliding with ball
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
        

#projectile is ball, so initializing ball
class Projectile(Sprite):
    def __init__(self, game, x, y,):
        self.game = game
        self.groups = game.all_sprites, game.all_projectiles
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(BLUE)
        self.rect.x = x 
        self.rect.y = y 
        #physics on ball with colliding, movement, etc
    def update(self):
        projectile_radius = 20
        projectile_x = WIDTH // 2
        projectile_y = HEIGHT // 2
        projectile_dx = 5  
        projectile_dy = 5  
        self.x += self.dx
        self.y += self.dy
        if projectile_x - projectile_radius <= 0 or projectile_x + projectile_radius >= WIDTH:
             projectile_dx = -projectile_dx
        if projectile_y - projectile_radius <= 0 or projectile_y + projectile_radius >= HEIGHT:
             projectile_dy = -projectile_dy

# collide ball with blocks
    def collide_with_stuff(self, group, kill):
        hits = pg.sprite.spritecollide(self, group, kill)
        projectile_radius = 20
        projectile_x = WIDTH // 2
        projectile_y = HEIGHT // 2
        projectile_dx = 5  
        projectile_dy = 5
    def update(self):
        hits = pg.sprite.spritecollide(self, self.game.all_projectiles, False)
        if hits:
            if str(hits[0].__class__.__name__) == "Block":
                print("I hit a block")
                hits = pg.sprite.spritecollide(self,self.game.all_projectiles, False)
                projectile_dx = -projectile_dx
                projectile_dy = -projectile_dy
    
        
#blocks on screen
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
    
        
#powerups class, still need to add  poweup release from collision of ball with block
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
        self.update()

    def update(self):
        pass


       