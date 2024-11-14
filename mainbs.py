import pygame as pg
from settingbs import *
from spritesbs import *
from os import path
from random import randint
from tilemapbs import *
'''

    
When player collides with enemy, bounces off
'''

'''
Sources: Mr. Cozort 1st game code'''

class Game:
    def __init__(self):
        #init initialies the screen and system below and the library of variables defined below
        pg.init()
        pg.mixer.init() #sound
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Breakout x Space Invaders")
        self.clock = pg.time.Clock()
        self.running = True
    def load_data(self):
        self.game_folder = path.dirname(__file__)
        self.map = Map(path.join(self.game_folder, 'level1.txt'))
    def new(self):
        self.load_data()
        print(self.map.data)
        self.all_sprites= pg.sprite.Group()
        self.all_walls = pg.sprite.Group()
        self.all_paddles = pg.sprite.Group()
        self.all_blocks = pg.sprite.Group()
        self.all_powerups = pg.sprite.Group()
        self.all_projectiles = pg.sprite.Group()
        self.player = paddle(self, 1, 1)


        for row, tiles in enumerate(self.map.data):
            print(row)
            for col, tile in enumerate(tiles):
                print(col)
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    paddle(self, col, row)
                if tile == 'B':
                    Block(self, col, row)
                if tile == 'U':
                    Powerup(self, col, row)
                if tile == 'A':
                    Projectile(self, col, row)
    
    def run(self):
        while self.running:
            #update evertyhing in sprite with four event definitions to define sprite
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    
        
        #create ball, physics for ball bounce of paddle

# allows for system to get new events occurring after keys pressed
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
#base code for creating base screen 
    def update(self):
        self.all_sprites.update()
    def draw_text(self, surface, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        surface.blit(text_surface, text_rect)

    def draw(self):
        self.screen.fill(WHITE)
        self.draw_text(self.screen, str(self.dt*1000), 24, BLACK, WIDTH/2, HEIGHT/2)
        self.draw_text(self.screen, "Powerups Collected: " + str(self.player.powerups), 24, BLACK, WIDTH/2, HEIGHT/24)
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    
if __name__ == "__mainbs__":
    print("main is running")
    g = Game()
    #creates all game elements with new method (not function)
    g.new()
    # run tha game
    g.run()
    print("main is running")
    
    