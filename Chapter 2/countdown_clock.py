import sys
import pygame
from random import randint

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#countdown time in seconds
START_TIME = 300

finished = False

pygame.init()

game_display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
game_display.fill(WHITE)
pygame.display.update()

# text display function, accepts string text input
def text_display(text):
    # our font is the pygame built-in, size 256
    text_font = pygame.font.Font(None, 256)
    text_surface = text_font.render(text, True, BLACK)
    text_rectangle = text_surface.get_rect()
    game_display.fill(WHITE)
    text_rectangle.center = (game_display.get_width()/2,
                             game_display.get_height()/2)
    #display the text
    game_display.blit(text_surface, text_rectangle)
    pygame.display.update()
    
while not finished:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            # if the key pressed is SPACE, start the timer
            if event.key == pygame.K_SPACE:
                for t in range(START_TIME, -1, -1):
                    minutes = t / 60
                    seconds = t % 60
                    sf = "{:02d}:{:02d}".format(*divmod(t, 60))               
                    game_display.fill(WHITE)
                    text_display(sf)
                    pygame.display.update()
        if event.type == pygame.QUIT:
            finished = True

    if time - pygame.time.get_ticks() >= 1000:
        clock_time -= 1
        time = pygame.time.get_ticks()

    if clock_time == 0:
        finished = True

    game_display.fill(WHITE)
    text_display(sf)
    pygame.display.update()
      
pygame.quit()
sys.exit()
