from python.core.particle import Particle
from python.core.vector import Vector

import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Engine")

particles = [
    Particle(
        pos=Vector(100, 100),
        velocity=Vector(0, 0),
        acceleration=Vector(0, 0),
        mass=2.5,
        force=None
    ),

    Particle(
        pos=Vector(300, 200),
        velocity=Vector(-5, 30),
        acceleration=Vector(0, 0),
        mass=5.5,
        force=None
    ),
]

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    for particle in particles:

        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(particle.pos.x), int(particle.pos.y)),
            10
        )

    pygame.display.flip()

    clock.tick(60)

pygame.quit()