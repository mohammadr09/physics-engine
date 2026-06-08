from python.physics.particle import Particle
from python.physics.forces.force import ForceGenerator

class World:
    def __init__(self) -> None:
        self.particles : list[Particle] = []
        self.force_generators : list[ForceGenerator] = []

    def append_particle(self, particle : Particle) -> None:
        self.particles.append(particle)

    def append_force_generator(self, force_generator : ForceGenerator) -> None:
        self.force_generators.append(force_generator)

    def update(self, dt : float) -> None:
        for particle in self.particles:
            for generator in self.force_generators:
                generator.update_force(particle)
            
            particle.apply(dt)