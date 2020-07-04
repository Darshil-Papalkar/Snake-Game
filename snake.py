import pygame
import time
import random 
from win32api import GetMonitorInfo , MonitorFromPoint

pygame.init()

monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
monitor_area = monitor_info.get("Monitor")


white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (12, 105, 47)
blue = (0, 183, 234)
dark_blue = (9, 9, 128)

dis_width = monitor_area[2]
dis_height = monitor_area[3]

dis = pygame.display.set_mode((dis_width, dis_height),pygame.FULLSCREEN)
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 10

font_style = pygame.font.SysFont("algerian", 35)
score_font = pygame.font.SysFont("arial black", 25,bold=True )
ins_font = pygame.font.SysFont("arial black", 15, bold=False, italic=False)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
    
def instructions():
    ins = ins_font.render('Press L-SHIFT to Restart',True,white)
    ins1 = ins_font.render('Press Esc to Exit',True,white)
    dis.blit(ins, [0, 35])
    dis.blit(ins1, [0,55])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        pygame.mixer.music.load('jazz.mp3')
        pygame.mixer.music.play(-1)

        while game_close == True:
            dis.fill(green)
            message("Press 'C' to Play Again or Press 'Q' to Quit", dark_blue)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            if x1 >= dis_width:
                x1 = 0
            elif x1 < 0:
                x1 = dis_width
            elif y1 >= dis_height:
                y1 = 0
            elif y1 < 0:
                y1 = dis_height

            #game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(green)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        '''for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True '''
        key_states = pygame.key.get_pressed()
        if key_states[pygame.K_ESCAPE]:
            pygame.quit()
        elif key_states[pygame.K_LSHIFT]:
            game_close = True


        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        instructions()
        

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
