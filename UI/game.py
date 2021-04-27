import tkinter as tk
import pygame


from UI.menu import Menu

class GameState():

    """This class handles the game state"""

    def __init__(self, window_dim):
        self.x = 120
        self.y = 120

        self.max_x = window_dim[0] - 40
        self.max_y = window_dim[1] - 40

    def update(self, moveCommandX, moveCommandY):
        self.x += moveCommandX
        self.y += moveCommandY

        if self.x < 0:
            self.x = 0
        if self.x > self.max_x:
            self.x = self.max_x
        
        if self.y < 0:
            self.y = 0
        if self.y > self.max_y:
            self.y = self.max_y

class UserInterface():

    """This class handles the game's user interface"""
    def __init__(self,args):
        pygame.init() # Initializes the window
        
        self.menus = {}
        
        self.menus['main_menu'] = {
            'options': [
                            {
                                'title': "Choose a Character",
                                'action': lambda: self.choose_character(args)
                            },
                            {
                                'title': "Quit",
                                'action': lambda: self.exit_menu()
                            }
                        ]
        }
        self.menus['main_menu']['window'] = Menu(args, self.menus['main_menu']['options'])
        self.current_window = self.menus['main_menu']['window']

        self.running = True

        """
        self.window_dim = (args['game_window_width'], args['game_window_height'])

        # makes a game window that is resizable
        self.window = pygame.display.set_mode(self.window_dim, flags=pygame.RESIZABLE) 
        pygame.display.set_caption(args['game_title'])

        # Clock to limit the fps
        self.clock = pygame.time.Clock()

        self.game_state = GameState(self.window_dim)
        self.running = True # For the game loop
        self.moveCommandX = 0
        self.moveCommandY = 0
        """

    def update(self):
        """Updates movement"""
        self.game_state.update(self.moveCommandX,
                               self.moveCommandY)

    def process_input(self):
        """Process the user input"""
        self.moveCommandX = 0
        self.moveCommandY = 0
        
        # Takes in the key input, and moves the 
        # box in that direction.
        
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_LEFT]:
            self.moveCommandX = -8
        if key_input[pygame.K_RIGHT]:
            self.moveCommandX = 8
        if key_input[pygame.K_UP]:
            self.moveCommandY = -8
        if key_input[pygame.K_DOWN]:
            self.moveCommandY = 8

        # pygame.event.get() needs to called in the main loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # Escape key to quit the game
                    self.running = False
                    break

                """if event.key == pygame.K_RIGHT:
                    pygame.key.set_repeat(50)
                    self.moveCommandX = 20
                if event.key == pygame.K_LEFT:
                    pygame.key.set_repeat(50)
                    self.moveCommandX = -20
                if event.key == pygame.K_DOWN:
                    pygame.key.set_repeat(50)
                    self.moveCommandY = 20
                if event.key == pygame.K_UP:
                    pygame.key.set_repeat(50)
                    self.moveCommandY = -20"""                      

    def render(self):
        self.window.fill((0,0,0))
        x = self.game_state.x
        y = self.game_state.y
        pygame.draw.rect(self.window, (0,0,255), (x,y,40,40))
        pygame.display.update()
    
    def exit_menu(self):
        """Exits the menu when player selects 'Quit'"""
        self.running = False
    
    def change_menu(self, menu_name):
        """Change the current menu"""
        self.current_window = self.menus[menu_name]['window']

    def choose_character(self, args):
        """A menu to choose a character"""
        if "character_menu" not in self.menus.keys():
            
            self.make_menu("character_menu", args,
            {'options': [
                            {
                                'title': "Back",
                                'action': lambda: self.change_menu("main_menu")
                            }
                        ]
            })
        self.change_menu("character_menu")

    def make_menu(self, menu_name, args, options):
        self.menus[menu_name] = options
        self.menus[menu_name]['window'] = Menu(args, self.menus[menu_name]['options'])


    def run(self):
        while self.running:
            #self.process_input()
            #self.update()
            #self.render()
            #self.clock.tick(60)

            self.current_window.process_input()
            self.current_window.update()
            self.current_window.render()
            self.current_window.clock.tick(60)

        pygame.quit()
