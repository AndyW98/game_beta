import pygame

class Button():
    """A customizable button that registers mouse clicks"""
    def __init__(self, x, y, sx, sy, bcolor, fbcolor, font, fontsize, fcolor, text):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.bcolor = bcolor
        self.fbcolor = fbcolor
        self.fcolor = fcolor
        self.fontsize = fontsize
        self.text = text
        self.current = False
        self.buttonf = pygame.font.SysFont(font, fontsize)
    
    def show_button(self, display):
        if(self.current):
            pygame.draw.rect(display, self.fbcolor, (self.x, self.y, self.sx, self.sy))
        
        else:
            pygame.draw.rect(display, self.bcolor, (self.x, self.y, self.sx, self.sy))
        
        textsurface = self.buttonf.render(self.text, False, self.fcolor)
        display.blit(textsurface,
                    (
                        (self.x + (self.sx/2) - (self.fontsize/2)*(len(self.text)/2 - 5)),
                        (self.y + (self.sy/2) - (self.fontsize/2) - 4)
                    )
                    )
    
    def focus_check(self, mousepos, mouseclick):
        if (
            mousepos[0] >= self.x 
            and mousepos[0] <= self.x + self.sx
            and mousepos[1] >= self.y
            and mousepos[1] <= self.y + self.sy
            ):
            self.current = True
            return mouseclick[0]
        
        else:
            self.current = False
            return False
