import pygame

from UI.screen import Screen

class Level(Screen):

    """This class handles a level"""
    def __init__(self, args, level_name, char_list):
        super().__init__(title=args['game_title'],
                         width=args['game_window_width'],
                         height=args['game_window_height'],
                         fill=args['colors']['main_window'])

        # Get level specific information
        self.level_info = args["levels"][level_name]

        # Grab the character list
        self.char_list = char_list;

        # Record the sprite directory
        self.sprite_dir = args["sprite_dir"]
        self.padding_x = args["levels"][level_name]["padding_x"]
        self.padding_y = args["levels"][level_name]["padding_y"]

        # Load the background image
        self.bg_image = pygame.image.load(args["map_dir"] + self.level_info["background"]).convert_alpha()
        self.bg_image = pygame.transform.smoothscale(self.bg_image,
                                                    (self.width-(2*self.padding_x),
                                                    self.height-(2*self.padding_y)))

        # Load the main character image
        self.main_char_img = pygame.image.load(args["sprite_dir"] + self.char_list["main_char"].sprite).convert_alpha()
        self.main_char_img = pygame.transform.smoothscale(self.main_char_img, (80,80))

    def update(self):
        """Update all sprite positions and character information"""
        self.heartbeat += 1

    def render(self):
        """Displays the level"""
        self.window.blit(self.bg_image, (self.padding_x,self.padding_y))

        self.render_chars()

        pygame.display.update()

    def render_chars(self):
        """Displays the character icons"""
        main_char_pos = self.char_list["main_char"].get_position()
        self.window.blit(self.main_char_img, (main_char_pos[0]+self.padding_x,main_char_pos[1]+self.padding_y))
    
    def process_input(self):
        """Processes the user's input in the level"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
                break

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.exit()
                    break
                if event.key == pygame.K_UP:
                    main_char_pos = self.char_list["main_char"].get_position()
                    self.char_list["main_char"].update_position(main_char_pos[0], main_char_pos[1]-1)
                if event.key == pygame.K_DOWN:
                    main_char_pos = self.char_list["main_char"].get_position()
                    self.char_list["main_char"].update_position(main_char_pos[0], main_char_pos[1]+1)
                if event.key == pygame.K_RIGHT:
                    main_char_pos = self.char_list["main_char"].get_position()
                    self.char_list["main_char"].update_position(main_char_pos[0]+1, main_char_pos[1])
                if event.key == pygame.K_LEFT:
                    main_char_pos = self.char_list["main_char"].get_position()
                    self.char_list["main_char"].update_position(main_char_pos[0]-1, main_char_pos[1])
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            main_char_pos = self.char_list["main_char"].get_position()
            self.char_list["main_char"].update_position(main_char_pos[0], main_char_pos[1]-1)
        if keys[pygame.K_DOWN]:
            main_char_pos = self.char_list["main_char"].get_position()
            self.char_list["main_char"].update_position(main_char_pos[0], main_char_pos[1]+1)
        if keys[pygame.K_RIGHT]:
            main_char_pos = self.char_list["main_char"].get_position()
            self.char_list["main_char"].update_position(main_char_pos[0]+1, main_char_pos[1])
        if keys[pygame.K_LEFT]:
            main_char_pos = self.char_list["main_char"].get_position()
            self.char_list["main_char"].update_position(main_char_pos[0]-1, main_char_pos[1])