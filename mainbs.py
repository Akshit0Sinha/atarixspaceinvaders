import pygame as pg
import random
from settingbs import *
from random import randint
'''

GOALS: destroy all blocks
RULES: don't let the ball fall down into the abyss
FEEDBACK: ball bouncing off block in __ direction
FREEDOM: moving the base below to track the ball

What sentence does your game make?
    
When player collides with enemy, bounces off
'''

class Game:
    def __init__(self):
        #init initialies the screen and system below and the library of variables defined below
        pg.init()
        pg.mixer.init() #sound
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Akshit's Game")
        self.clock = pg.time.Clock()
        self.running = True
    def new(self):
        # create place for paddle, blocks to destroy, and powerups to create after destroying blocks
        self.load_data()
        print(self.map.data)
        self.paddle = pg.sprite.Group()
        
        #create ball, physics for ball bounce of paddle

# allows for system to get new events occurring after keys pressed
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
#base code for creating base screen 
    def draw(self):
        self.screen.fill(WHITE)
        self.draw_text(self.screen, str(self.dt*1000), 24, BLACK, WIDTH/2, HEIGHT/2)
        self.draw_text(self.screen, "Coins Collected: " + str(self.player.coins), 24, BLACK, WIDTH/2, HEIGHT/24)
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    
    