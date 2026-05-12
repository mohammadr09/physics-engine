from python.physics.particle import Particle

class World:
    def __init__(self) -> None:
        self.particles = []
        self.force_generators = []

    def update(self, dt):
        ...