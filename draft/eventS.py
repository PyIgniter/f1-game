
"""

"""
import pygame

WIN_WIDTH = 560
board_width = WIN_WIDTH - 60
WIN_HEIGTH = 590
board_heigth = WIN_HEIGTH - 60
DISPLAY = (WIN_WIDTH, WIN_HEIGTH)
BACKGROUND_COLOR = (0, 50, 0)


def main():
    pygame.init()
    window = pygame.display.set_mode((DISPLAY)) #Create Window
    pygame.display.set_caption('Some game') # Write in the window cap
    # Creating a Visible Surface will be used as a background
    screen = pygame.Surface(DISPLAY)
    # sring events
    info_string = pygame.Surface((WIN_WIDTH, 30))

    
    class Sprite:
        def __init__(self, xpos, ypos, filename):
            self.x = xpos
            self.y = ypos
            self.bitmap = pygame.image.load(filename)
            # background 
            # self.bitmap.set_colorkey((0,50,0))

        def render(self):
            screen.blit(self.bitmap, (self.x, self.y))

    def Intersect(x1, x2, y1, y2, db1, db2):
        if (x1 > x2-db1) and (x1 < x2+db2) and (y1 > y2-db1) and (y1 < y2+db2):
            return 1
        else:
            return 0
    # Init fonts
    pygame.font.init()
    speed_font = pygame.font.Font(None, 32)
    label_font = pygame.font.SysFont('eufm10', 24)
    inf_font = pygame.font.SysFont('Comic Sans MS', 24)
    # Initial hero
    hero = Sprite(250, 350, 'arrow.gif') 
    # Initial target
    target = Sprite(10, 10, 'target.gif')
    target.right = False
    target.step = 1
    enumerator = 0
    sniper_color = 255
    # Initial ball
    ball = Sprite(-10, 650, 'ball.gif')
    ball.push = False
            

    done = True
    pygame.key.set_repeat(1, 1)
    while done:
        # Processing Events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = False

        # events keys down
        if e.type == pygame.KEYDOWN:
            # movement of the hero along the Х axis
            if e.key == pygame.K_LEFT:
                if hero.x > 10:
                    hero.x -= 1
            if e.key == pygame.K_RIGHT:
                if hero.x < board_width:
                    hero.x += 1
            # movement of the hero along the Y axis
            if e.key == pygame.K_UP:
                if hero.y > 200:
                    hero.y -= 1
            if e.key == pygame.K_DOWN:
                if hero.y < board_heigth:
                    hero.y += 1
            # launch ball
            if e.key == pygame.K_SPACE:
                if ball.push == False:
                    ball.x = hero.x + 5
                    ball.y = hero.y 
                    ball.push = True
        # events mouse moution
        if e.type == pygame.MOUSEMOTION:
            pygame.mouse.set_visible(False)
            m = pygame.mouse.get_pos()
            if m[0] > 10 and m[0] < board_width:
                hero.x = m[0]
            if m[1] > 200 and m[1] < board_heigth:
                 hero.y = m[1]
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                if ball.push == False:
                    ball.x = hero.x + 5
                    ball.y = hero.y 
                    ball.push = True

        #Fill the surface with solid color
        screen.fill(BACKGROUND_COLOR)
        info_string.fill((45, 80, 40))
        # color
        sniper_color += 0.1
        if sniper_color > 254:
            sniper_color = 100
        # movement of the target
        if target.right == True:
            target.x -= target.step
            if target.x < 0:
                target.right = False
        else:
            target.x += target.step
            if target.x > 500:
                target.right = True
        # movement of the ball
        if ball.y < 0:
            ball.push = False
            enumerator -= 1

        if ball.push == False:
            ball.y = 650
            ball.x = -40
        else:
            ball.y -= 1

        # 
        if Intersect(ball.x, target.x, ball.y, ball.y, 50, 5) == True:
            ball.push = False
            target.step += 0.2
            enumerator += 1 


        # Each iteration needs to be redrawn
        # rendering object
        ball.render()
        target.render()
        hero.render()
        # rendering fonts
        info_string.blit(speed_font.render(u'Speed :'+str(target.step), 1, (210, 120, 200)), (250, 5))
        info_string.blit(label_font.render(u'SNIPER', 1, (0, sniper_color, 0)), (120, 5))
        info_string.blit(inf_font.render(u'Nums :'+str(enumerator), 1, (0, 250, 200)), (10, 0) )
        # view screen
        window.blit(info_string, (0, 0))
        window.blit(screen, (0, 30))
        pygame.display.flip()
        pygame.time.delay(5)

if __name__ == "__main__":
    main()


