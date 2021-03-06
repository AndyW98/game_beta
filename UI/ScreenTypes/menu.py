import pygame

from UI.screen import Screen
from UI.objects import Button

class Menu(Screen):

    """An abstract class to handle menus"""

    def __init__(self, args, menu_items=[]):
        super().__init__(title=args['game_title'],
                         width=args['game_window_width'],
                         height=args['game_window_height'],
                         fill=args['colors']['main_window'])

        # Set fonts
        title_font_loc = pygame.font.match_font(args['game_title_font'])
        txt_font_loc = pygame.font.match_font(args['game_text_font'])
        self.title_font = pygame.font.Font(title_font_loc, 72)
        self.item_font = pygame.font.Font(txt_font_loc, 20)
        
        # Colors
        self.bg_color = args['colors']

        default_menu_items = \
        [
            {
                'title': "Item1",
                'action': lambda: self.action()
            },
            {
                'title': "Quit",
                'action': lambda: self.exit_menu()
            }
        ]
        if not menu_items:
            self.menu_items = default_menu_items
        else:
            self.menu_items = menu_items
        
        self.current_menu_item = 0
        
        # Loads cursor
        self.menu_cursor = pygame.image.load(args['sprite_dir'] + args['cursor_image'])
        self.menu_cursor = pygame.transform.scale(self.menu_cursor,
                                                  (43, 43))

    def action(self):
        """An action to do when selected"""
        print("This is an action")

    def process_input(self):
        """Processes the user's input in the menu"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
                break            
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and self.current_menu_item < len(self.menu_items) - 1:
                    self.current_menu_item += 1
                
                elif event.key == pygame.K_UP and self.current_menu_item > 0:
                    self.current_menu_item -= 1
                
                elif event.key == pygame.K_RETURN:
                    # When the user selects the option, do the appropriate action
                    menu_item = self.menu_items[self.current_menu_item]
                    try:
                        menu_item['action']()
                    except Exception as ex:
                        print(ex)
                
                elif event.key == pygame.K_ESCAPE:
                    self.exit()
                    break

    def render(self):
        """Displays the menu"""
        self.window.fill(self.bg_color['main_window'])

        # Initial y
        y = 50

        # Title
        surface = self.title_font.render("Game Beta", True, self.bg_color['title_color'])

        x = (self.window.get_width() - surface.get_width()) / 2
        self.window.blit(surface, (x,y))
        y += (200 * surface.get_height()) / 100

        # Compute menu width
        menu_width = 0
        for item in self.menu_items:
            surface = self.item_font.render(item['title'], True, (0, 0, 200))
            menu_width = max(menu_width, surface.get_width())
            item['surface'] = surface
        
        # Draw menu items
        x = (self.window.get_width() - menu_width) / 2
        for i, item in enumerate(self.menu_items):
            # Item text
            surface = item['surface']
            self.window.blit(surface, (x, y))

            # Cursor
            if i == self.current_menu_item:
                cursorX = x - self.menu_cursor.get_width() - 10
                cursorY = y + (surface.get_height() - self.menu_cursor.get_height()) / 2
                self.window.blit(self.menu_cursor, (cursorX, cursorY))

            y += (120 * surface.get_height()) / 100

        pygame.display.update()

    def run(self):
        """Runs the menu"""
        while self.running:
            self.process_input()
            self.update()
            self.render()
            self.clock.tick(60)