# import tkinter as tk
import pygame


from UI.ScreenTypes.menu import Menu
from UI.ScreenTypes.level import Level

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
    def __init__(self, item_list, char_list, args):
        pygame.init() # Initializes the window
        
        self.char_list = char_list
        self.item_list = item_list
        self.args      = args

        # Add menus to the window
        self.menus = {
            'main_menu': {
                'options': [
                    {
                        'title': "Choose a Character",
                        'action': lambda: self.change_menu("character_menu")
                    },
                    {
                        'title': "View Items",
                        'action': lambda: self.change_menu("items_menu")
                    },
                    {
                        'title': "View Levels",
                        'action': lambda: self.change_menu("levels_menu")
                    },
                    {
                        'title': "Quit",
                        'action': lambda: self.exit_menu()
                    }
                ]
            },
            'character_menu': {
                'options': [
                    {
                        'title': "Back",
                        'action': lambda: self.change_menu("main_menu")
                    }
                ]
            },
            'items_menu': {
                'options': [
                    {
                        'title': "Back",
                        'action': lambda: self.change_menu("main_menu")
                    }
                ]
            },
            'levels_menu': {
                'options': [
                    {
                        'title': "Level 1",
                        'action': lambda: self.open_level("level_1")
                    },
                    {
                        'title': "Back",
                        'action': lambda: self.change_menu("main_menu")
                    }
                ]
            }
        }

        # Add character stat printouts to console
        for char in self.char_list.keys():
            opt = {
                'title': char,
                'action': self.print_char_to_console(char)
            }
            self.menus['character_menu']['options'].insert(0, opt)
        
        # Add item stat printouts to console
        for item in self.item_list.keys():
            opt = {
                'title': item,
                'action': self.print_item_to_console(item)
            }
            self.menus['items_menu']['options'].insert(0, opt)

        # Initialize each menu
        for menu in self.menus.keys():
            self.menus[menu]['window'] = Menu(self.args, self.menus[menu]['options'])

        # Set the current window to the main menu
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

    def print_char_to_console(self, char_name):
        """Pretty print the character stats to console"""
        return lambda: self.char_list[char_name].pretty_print_stats()
    
    def print_item_to_console(self, item_name):
        """Print the item stats to console"""
        return lambda: print(self.item_list[item_name].__str__())

    def exit_menu(self):
        """Exits the menu when player selects 'Quit'"""
        self.running = False
    
    def change_menu(self, menu_name):
        """Change the current menu"""
        self.current_window.end_current()
        self.current_window = self.menus[menu_name]['window']
    
    def open_level(self, level_name):
        """Open the named level"""
        self.current_window.end_current()
        self.current_window = Level(self.args, level_name, self.char_list)

    def make_menu(self, menu_name, args, options):
        """Make a new menu with options"""
        self.menus[menu_name] = options
        self.menus[menu_name]['window'] = Menu(args, self.menus[menu_name]['options'])

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
        """Render the window state"""
        self.window.fill((0,0,0))
        x = self.game_state.x
        y = self.game_state.y
        pygame.draw.rect(self.window, (0,0,255), (x,y,40,40))
        pygame.display.update()


    def run(self):
        """Main control loop"""
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
