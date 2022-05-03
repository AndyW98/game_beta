import pygame

colors = {
    "White": (255, 255, 255),
    "Black": (0, 0, 0),
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255)
}

class Screen():
    """A pygame screen"""
    def __init__(self, title, width=640, height=445, fill=colors['White']):
        self.title = title
        self.width = width
        self.height = height
        self.fill = fill
        self.current = False

        # Initialize the window
        pygame.init()
        self.window_dim = (width, height)
        self.window = pygame.display.set_mode(self.window_dim)
        pygame.display.set_caption(title)

        # Game loop properties
        self.clock = pygame.time.Clock()
        self.running = True

        # Make this window the current window
        self.make_current()
    
    def make_current(self):
        self.current = True
        pygame.display.set_caption(self.title)
        self.screen = pygame.display.set_mode((self.width, self.height))
    
    def end_current(self):
        self.current = False
    
    def check_update(self):
        return self.current

    def update(self):
        """May need later"""
        pass

    def screen_update(self):
        if(self.current):
            self.screen.fill(self.fill)
    
    def return_title(self):
        return self.screen
    
    def exit(self):
        """Exit the screen"""
        self.running = False
    
    """
    Virtual Functions
    """
    def render(self):
        """Virtual function for rendering the screen"""
        raise NotImplementedError()
    
    def process_input(self):
        """Virtual function for processing input on the screen"""
        raise NotImplementedError()