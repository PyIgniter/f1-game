
"""

"""
import pygame, sys

WIN_WIDTH = 560
board_width = WIN_WIDTH - 70
WIN_HEIGTH = 590
board_heigth = WIN_HEIGTH - 35
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
    # movement area
    target_area = pygame.Surface((540, 60))
    hero_area = pygame.Surface((540, 350))

    
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

    class Menu:
        """docstring for Menu"""
        def __init__(self, punkts = [220, 140, u'Punkt', (0, 0, 255), (255, 0, 255), 0]):
            self.punkts = punkts
        def render(self, plot, font, num_punkt):
            for i in self.punkts:
                if num_punkt == i[5]:
                    plot.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
                else:
                    plot.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
        def menu(self):
            done = True
            font_menu = pygame.font.Font('fonts/11610.ttf', 60)
            pygame.key.set_repeat(0, 0)
            pygame.mouse.set_visible(True)
            punkt = 0
            while done:
                screen.fill((119, 136, 153))

                mp = pygame.mouse.get_pos()
                for i in self.punkts:
                    if mp[0] > i[0] and mp[0] < i[0] + 145 and mp[1] > i[1] and mp[1] < i[1] + 55:
                        punkt = i[5]
                self.render(screen, font_menu, punkt)

                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        sys.exit()
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_ESCAPE:
                            sys.exit()
                        if e.key == pygame.K_UP:
                            if punkt > 0:
                                punkt -= 1
                        if e.key == pygame.K_DOWN:
                            if punkt < len(self.punkts) - 1:
                                punkt += 1
                    if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                        if punkt == 0:
                            done = False
                        elif punkt == 1:
                            sys.exit()

                window.blit(screen, (0, 0))
                pygame.display.flip()

    # Init fonts
    pygame.font.init()
    speed_font = pygame.font.Font('fonts/11602.ttf', 18)
    label_font = pygame.font.Font('fonts/11610.ttf', 26)
    inf_font = pygame.font.Font('fonts/11602.ttf', 18)
    # Initial hero
    hero = Sprite(250, 350, 'sprites/player.png') 
    # Initial target
    target = Sprite(10, 10, 'sprites/basket.png')
    target.right = False
    target.step = 1
    
    # Initial ball
    ball = Sprite(-10, 550, 'sprites/ball.png')
    ball.push = False
         
    # create Menu
    punkts = [
    (220, 140, u'Play', (0, 0, 255), (250, 30, 250), 0),
    (230, 210, u'Exit', (0, 0, 255), (250, 30, 250), 1)
    ]
    game = Menu(punkts)
    game.menu()

    # podgotovka to launch game   
    done = True
    pygame.key.set_repeat(1, 1)
    pygame.mouse.set_visible(False)
    enumerator = 0
    sniper_color = 255
    while done:
        # Processing Events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = False

            # events keys down
            if e.type == pygame.KEYDOWN:
                # movement of the hero along the Х axis
                if e.key == pygame.K_LEFT:
                    if hero.x > 0:
                        hero.x -= 1
                if e.key == pygame.K_RIGHT:
                    if hero.x < board_width:
                        hero.x += 1
                # movement of the hero along the Y axis
                if e.key == pygame.K_UP:
                    if hero.y > 200:
                        hero.y -= 1
                if e.key == pygame.K_DOWN:
                    if hero.y < board_heigth - 60:
                        hero.y += 1
                # launch ball
                if e.key == pygame.K_SPACE:
                    if ball.push == False:
                        ball.x = hero.x + 5
                        ball.y = hero.y 
                        ball.push = True
                if e.key == pygame.K_ESCAPE:
                    game.menu()
                    pygame.key.set_repeat(1, 1)
                    pygame.mouse.set_visible(False)
            # events mouse moution
            if e.type == pygame.MOUSEMOTION:
                pygame.mouse.set_visible(False)
                m = pygame.mouse.get_pos()
                if m[0] > 0 and m[0] < board_width:
                    hero.x = m[0]
                if m[1] > 200 and m[1] < board_heigth - 60:
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
            if target.x < 5:
                target.right = False
        else:
            target.x += target.step
            if target.x > 490:
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
        if Intersect(ball.x, target.x, ball.y, target.y, 50, 60) == True:
            ball.push = False
            target.step += 0.2
            enumerator += 1 


        # Each iteration needs to be redrawn
        # rendering object
        screen.blit(target_area, (10, 10))
        screen.blit(hero_area, (10, 200))
        ball.render()
        target.render()
        hero.render()
        
        # rendering fonts
        info_string.blit(speed_font.render(u'Speed :'+str(target.step), 1, (210, 120, 200)), (370, 5))
        info_string.blit(label_font.render(u'Basketball', 1, (0, sniper_color, 0)), (10, 5))
        info_string.blit(inf_font.render(u'Points:'+str(enumerator), 1, (0, 250, 200)), (270, 5) )
        # view screen
        window.blit(info_string, (0, 0))
        window.blit(screen, (0, 30))
        pygame.display.flip()
        pygame.time.delay(5)

if __name__ == "__main__":
    main()


