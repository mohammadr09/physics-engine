from abc import ABC, abstractmethod
from python.physics.particle import Particle
from python.core.vector import Vector

class ForceGenerator(ABC):

    @abstractmethod
    # get_force(self, particle : Particle) -> Vector
    # Returns the force acting upon the object
    def get_force(self, particle : Particle) -> Vector:
        pass

    @abstractmethod
    # update_force(self, particle : Particle) -> None
    # Adds the force onto the particle.
    def update_force(self, particle : Particle) -> None:
        pass