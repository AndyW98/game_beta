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
    
    def render(self):
        """Displays the level"""
        self.window.fill()