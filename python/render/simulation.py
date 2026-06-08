from python.physics.particle import Particle
from python.core.vector import Vector
from python.physics.world import World
from python.physics.forces.gravity import Gravity
from python.physics.forces.drag import Drag
import random
import math

import pygame

pygame.init()
clock = pygame.time.Clock()

WIDTH = 800
HEIGHT = 600
RADIUS = 10

world = World()
gravity = Gravity(-9.8)
drag = Drag(20, 0.28, math.pi * (RADIUS ** 2))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Engine • Python Prototype")

ball = Particle(
    Vector(400,300),
    Vector(0,0),
    Vector(0,0),
    RADIUS
)

world.append_particle(ball)
world.append_force_generator(gravity)
# world.append_force_generator(drag)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))
    dt = clock.tick(60) / 1000

    world.update(dt)

    for particle in world.particles:
        print(type(particle.pos.x))
        print(type(particle.pos.y))
        print(particle.pos)

        pygame.draw.circle(
            screen,
            particle.color,
            (int(particle.pos.x), int(particle.pos.y)), 
            RADIUS
        )

        if particle.pos.y >= HEIGHT - RADIUS:
            particle.pos.y = HEIGHT - RADIUS
            particle.velocity.y *= -0.8
        elif particle.pos.y <= 0 - RADIUS:
            particle.pos.y = 0
            particle.velocity.y *= -0.8

        if particle.pos.x >= WIDTH - RADIUS:
            particle.pos.x = WIDTH - RADIUS
            particle.velocity.x *= -0.8
        elif particle.pos.x <= 0 - RADIUS:
            particle.pos.x = 0
            particle.velocity.x *= -0.8

    pygame.display.flip()

pygame.quit()