from bird import Bird
from base import Base
from pipe import Pipe
from const import *
from utils import draw_window
import pygame

if __name__ == '__main__':
    bird = Bird(230, 350)
    base = Base(730)
    pipes = [Pipe(700)]
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    run = True

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_window(win, bird, pipes, base)
    
    pygame.quit()
    quit()

