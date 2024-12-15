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
        self.playing = True
        self.score = 0
    def load_data(self):
        self.game_folder = path.dirname(__file__)
        # load high score file
        # from chagpt - prompt: with open create file in python
        with open(path.join(self.game_folder, HS_FILE), 'w') as file:
            file.write("High Score File!")
        print("file created and written successfully.")
        
        with open(path.join(self.game_folder, HS_FILE), 'r') as f:
             try:
                self.highscore = int(f.read())
             except:
                self.highscore = 0
        self.img_folder = path.join(self.game_folder, 'images')
        self.snd_folder = path.join(self.game_folder, 'sounds')
        self.map = Map(path.join(self.game_folder, 'level1.txt'))
       #self.shoot_snd = pg.mixer.Sound(path.join)

    def new(self):
        self.load_data()
        print(self.map.data)
        self.all_sprites= pg.sprite.Group()
        self.all_walls = pg.sprite.Group()
        self.all_paddles = pg.sprite.Group()
        self.all_blocks = pg.sprite.Group()
        self.all_powerups = pg.sprite.Group()
        self.all_projectiles = pg.sprite.Group()
        self.player = paddle(self, 101, 101)
        #self.check_highscore()


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
    # def check_highscore(self):
    #   # if the file exists
    #     if path.exists(HS_FILE):
    #       print("this exists...")
    #       with open(path.join(self.game_folder, HS_FILE), 'r') as f:
    #             self.best_time = int(f.read())
    #     else:
    #       with open(path.join(self.game_folder, HS_FILE), 'w') as f:
    #             f.write("0")
    #             self.best_time =  100000
    #             f.write(str(100000))
    #     print("File created and written successfully.")
    
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
                if self.score > self.highscore:
                    self.highscore = self.score
                    with open(path.join(self.game_folder, HS_FILE), 'w') as f:
                        f.write(str(self.score))
            if self.playing:
                self.playing = False
            self.running = True
            if event.type == pg.K_r:
                if event.key == pg.K_ESCAPE:  # Example: press Escape to quit
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
        #self.draw_text(self.screen, "Powerups Collected: " + str(self.player.powerups), 24, BLACK, WIDTH/2, HEIGHT/24)
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    def show_go_screen(self):
        self.game_folder = path.dirname(__file__)
        # game over/continue
        
        #if path.exists(HS_FILE):
         # print("this exists...")
          #with open(path.join(self.game_folder, HS_FILE), 'r') as f:
           #     self.highscore = int(f.read())
        #else:
         # with open(path.join(self.game_folder, HS_FILE), 'w') as f:
          #        f.write(str(0))
        print("File created and written successfully.")
        self.screen.fill(WHITE)
        #end screen
        if not self.running:
            self.draw_text(self.screen, "Restart", 48, BLACK, WIDTH / 2, HEIGHT / 4)
            pg.display.flip()
            self.wait_for_key()

    def show_end_screen(self):
        print("File created and written successfully.")
        self.screen.fill(BLACK)
        self.draw_text(self.screen, "You're done! ", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text(self.screen, "Best time: " + str(self.best_time), 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text(self.screen, "Press a key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    
    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False
    
if __name__ == "__main__":
    print("main is running")
    g = Game()
    #creates all game elements with new method (not function)
    g.show_go_screen()
    while g.playing:
        g.new()
        g.run()
    print("main is running")