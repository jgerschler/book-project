import sys
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

finished = False
minutes = 2
seconds = 39

def text_display(text):
    text_font = pygame.font.Font(None, 256)
    text_surface = text_font.render(text, True, BLACK)
    text_rectangle = text_surface.get_rect()
    game_display.fill(WHITE)
    text_rectangle.center = (game_display.get_width()/2,
                             game_display.get_height()/2)
    game_display.blit(text_surface, text_rectangle)
    pygame.display.update()

def timer(minutes, seconds):
    starting_ticks = pygame.time.get_ticks()
    time_remaining = minutes * 60 + seconds
    while time_remaining > 0:
        current_ticks = pygame.time.get_ticks()
        if current_ticks - starting_ticks > 1000:
            time_remaining -= 1
            starting_ticks = pygame.time.get_ticks()
        text_display("{:02d}:{:02d}".format(*divmod(time_remaining, 60)))
    pygame.time.wait()
    text_display("{:02d}:{:02d}".format(minutes, seconds))

pygame.init()

game_display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
game_display.fill(WHITE)
text_display("{:02d}:{:02d}".format(minutes, seconds))
pygame.display.update()

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE:
                timer(minutes, seconds)
        if event.type == pygame.QUIT:
            finished = True
      
pygame.quit()
sys.exit()
