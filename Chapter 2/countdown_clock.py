import sys
import pygame
from random import randint

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# countdown time in seconds
clock_time = 30
# clock time digit formatting
sf = "{:02d}:{:02d}".format(*divmod(clock_time, 60)) 

finished = False
timer_started = False

pygame.init()

game_display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
game_display.fill(WHITE)
pygame.display.update()

def text_display(text):
    text_font = pygame.font.Font(None, 256)
    text_surface = text_font.render(text, True, BLACK)
    text_rectangle = text_surface.get_rect()
    game_display.fill(WHITE)
    text_rectangle.center = (game_display.get_width()/2,
                             game_display.get_height()/2)
    game_display.blit(text_surface, text_rectangle)
    pygame.display.update()
    
while not finished:
    # if timer is started, start counting down
    if timer_started == True:
        if pygame.time.get_ticks() - total_time >= 1000:
            clock_time -= 1
            total_time = pygame.time.get_ticks()
            minutes = clock_time / 60
            seconds = clock_time % 60
            sf = "{:02d}:{:02d}".format(*divmod(clock_time, 60))    
            
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE:
                # if spacebar is pressed, get current ticks
                # and start timer
                total_time = pygame.time.get_ticks()
                timer_started = True
        if event.type == pygame.QUIT:
            finished = True

    if clock_time == 0:
        finished = True

    game_display.fill(WHITE)
    # display time and update screen
    text_display(sf)
    pygame.display.update()
      
pygame.quit()
sys.exit()
