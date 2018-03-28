
"""

"""
import pygame

WIN_WIDTH = 800
board_width = WIN_WIDTH - 111
WIN_HEIGTH = 700
board_heigth = WIN_HEIGTH - 111
DISPLAY = (WIN_WIDTH, WIN_HEIGTH)
BACKGROUND_COLOR = (0, 50, 0)


def main():
    pygame.init()
    window = pygame.display.set_mode((DISPLAY)) #Create Window
    pygame.display.set_caption('Some game') # Write in the window cap
    # Creating a Visible Surface will be used as a background
    screen = pygame.Surface(DISPLAY)
    
    class Sprite:
        def __init__(self, xpos, ypos, filename):
            self.x = xpos
            self.y = ypos
            self.bitmap = pygame.image.load(filename)
            self.bitmap.set_colorkey((0,50,0))

        def render(self):
            screen.blit(self.bitmap, (self.x, self.y))

    def Intersect(x1, x2, y1, y2):
        if (x1 > x2-111) and (x1 < x2+111) and (y1 > y2-111) and (y1 < y2+111):
            return 1
        else:
            return 0

    hero = Sprite(222, 350, 'ball.gif') 
    hero.go_right = True
    hero.go_down = True
    zet = Sprite(222, 10, 'ball.gif')
    zet.go_down = False
            
    done = True
    while done:
        # Processing Events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = False
        #Fill the surface with solid color
        screen.fill(BACKGROUND_COLOR) 
        
        if hero.go_down == True:
            hero.y -= 1
            if hero.y == 0:
                hero.go_down = False
        else:
            hero.y += 1
            if hero.y == board_heigth:
                hero.go_down = True
        
        if zet.go_down == True:
            zet.y -= 1
            if zet.y == 0:
                zet.go_down = False
        else:
            zet.y += 1
            if zet.y == board_heigth:
                zet.go_down = True
        if Intersect(zet.x, hero.x, zet.y, hero.y) == True:
            hero.go_down = False
            zet.go_down = True

        # Each iteration needs to be redrawn
        # screen.blit(square,(x, y))
        zet.render()
        hero.render()
        window.blit(screen, (0, 0))
        pygame.display.flip()
        pygame.time.delay(5)

if __name__ == "__main__":
    main()


