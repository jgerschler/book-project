# import modules
import sys
import pygame

# define color white (red, green, blue) (0-255)
WHITE = (255, 255, 255)

# is the game finished?
finished = False

# initialize pygame
pygame.init()

# set our display as fullscreen
game_display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# set the background color as white
game_display.fill(WHITE)
# update the display
pygame.display.update()

# main loop, do this while game is not finished (finished = False)
while not finished:
    # cycle through events in the queue
    for event in pygame.event.get():
        # if a key has been pushed and released
        if event.type == pygame.KEYUP:
            # and if that key is ESCAPE, quit!
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        # if a different quit event is detected, quit
        if event.type == pygame.QUIT:
            # finished = True, so we exit loop
            finished = True

# if we've exited the loop, we quit!        
pygame.quit()
sys.exit()
