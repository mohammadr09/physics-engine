from core.particle import Particle
from core.vector import Vector

import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Engine")

particles = [
    Particle(pos=Vector(0,0), velocity=Vector(0,0), acceleration=Vector(0,0), mass=2.5, force=None),
    Particle(pos=Vector(5,30), velocity=Vector(-5,30), acceleration=Vector(0,0), mass=5.5, force=None),
    ]

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for particle in particles:
        screen.fill(random.randint(0,255), None, random.randint(0,255))
        

pygame.quit()