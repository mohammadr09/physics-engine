from python.physics.particle import Particle

class World:
    def __init__(self) -> None:
        self.particles : list[Particle] = []

    def update(self, dt : float) -> None:
        for particle in self.particles:
            particle.apply(dt)