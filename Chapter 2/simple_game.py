import sys
import pygame
from random import randint

WHITE = (255, 255, 255)
# the color black
BLACK = (0, 0, 0)

finished = False
game_phrases = ["10 Points", "20 Points", "30 Points", "40 Points", "-50 Points", "LOSE TURN"]

pygame.init()

game_display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
game_display.fill(WHITE)
pygame.display.update()

# text display function, accepts string text input
def text_display(text):
    # our font is the pygame built-in, size 256
    text_font = pygame.font.Font(None, 256)
    # our text surface is created by rendering the text
    # using the chosen font
    text_surface = text_font.render(text, True, BLACK)
    # get the rectangle for our text surface
    text_rectangle = text_surface.get_rect()
    # fill the display with white
    game_display.fill(WHITE)
    # center the text by centering its rectangle
    text_rectangle.center = (game_display.get_width()/2,
                             game_display.get_height()/2)
    #display the text
    game_display.blit(text_surface, text_rectangle)
    # update the display
    pygame.display.update()
    
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            # if the key pressed is SPACE, send a random
            # game phrase string to the text_display function
            if event.key == pygame.K_SPACE:
                # select random entry from game_phrases list
                text_display(game_phrases[randint(0, len(game_phrases) - 1)])
        if event.type == pygame.QUIT:
            finished = True
      
pygame.quit()
sys.exit()
