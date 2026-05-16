from python.physics.particle import Particle
from python.core.vector import Vector
import random

import pygame

pygame.init()
clock = pygame.time.Clock()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Engine Python Prototype")

particles = [
    Particle(
        pos=Vector(0, 0),
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

GRAVITY = Vector(0, 500)
RADIUS = 10

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))
    dt = clock.tick(60) / 1000

    for particle in particles:
        pygame.draw.circle(
            screen,
            particle.color,
            (int(particle.pos.x), int(particle.pos.y)), 
            RADIUS
        )
        
        f_g = GRAVITY * particle.mass
        particle.apply_force(f_g)
        particle.apply(dt)

        if particle.pos.y >= HEIGHT - RADIUS:
            particle.pos.y = HEIGHT - RADIUS
            particle.velocity.y *= -0.8

        if particle.pos.x >= WIDTH - RADIUS:
            particle.pos.x = WIDTH - RADIUS
            particle.velocity.x *= -0.8

    pygame.display.flip()

pygame.quit()