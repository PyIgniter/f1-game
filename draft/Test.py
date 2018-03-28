
"""

"""
import pygame

WIN_WIDTH = 400
WIN_HEIGTH = 500
DISPLAY = (WIN_WIDTH, WIN_HEIGTH)
BACKGROUND_COLOR = (0, 50, 0)


def main():
    pygame.init()
    window = pygame.display.set_mode((DISPLAY)) #Create Window
    pygame.display.set_caption('Some game') # Write in the window cap
    # Creating a Visible Surface will be used as a background
    scrren = pygame.Surface(DISPLAY)
    
    # object square
    square = pygame.Surface((40, 40))
    square.fill((0, 255, 0))

    x = 0
    y = 0
    square_go_right = True
    square_go_down = True
    done = True
    while done:
        # Processing Events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = False
        #Fill the surface with solid color
        scrren.fill(BACKGROUND_COLOR) 
        #move os x
        if square_go_right == True:
            x += 1
            if x > 360:
                square_go_right = False
        else:
            x -= 1
            if x < 0:
                square_go_right = True
        #move os y
        if square_go_down == True:
            y += 1
            if y > 360:
                square_go_down = False
        else:
            y -= 1
            if y < 0:
                square_go_down = True
    
        # Each iteration needs to be redrawn
        scrren.blit(square,(x, y))
        window.blit(scrren, (0, 0))
        #Update and display all changes on the screen
        pygame.display.update()
        pygame.display.flip()
        pygame.time.delay(500)

if __name__ == "__main__":
    main()


