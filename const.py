import pygame
import os

WIDTH = 600
HEIGHT = 800

BIRD_IMGS = [
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bard1.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bard2.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bard3.png")))
]

PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))

BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))

BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))