import pygame

from UI.screen import Screen

class Level(Screen):

    """This class handles a level"""
    def __init__(self, args, level_name):
        super().__init__(title=args['game_title'],
                         width=args['game_window_width'],
                         height=args['game_window_height'],
                         fill=args['colors']['main_window'])

        # Get level specific information
        self.level_info = args["levels"][level_name]

        # Load the background image
        self.bg_image = pygame.image.load(args["map_dir"] + self.level_info["background"])
    
    def render(self):
        """Displays the level"""
        self.window.blit(self.bg_image, (0,0))

        pygame.display.update()
    
    def process_input(self):
        """Processes the user's input in the level"""
        for event in pygame.event.get():
            pass