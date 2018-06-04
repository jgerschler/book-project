import sys
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

START_TIME_SEC = 60

finished = False

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
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            # if the key pressed is SPACE, send a random
            # integer string to the text_display function
            if event.key == pygame.K_SPACE:
                                            minutes = t / 60
                            seconds = t % 60
                            sf = "{:02d}:{:02d}".format(*divmod(t, 60))
                text_display(str(randint(1, 10)))
        if event.type == pygame.QUIT:
            finished = True
      
pygame.quit()
sys.exit()
