from python.physics.forces.force import ForceGenerator
from python.physics.particle import Particle
from python.core.vector import Vector

from typing import Optional
import math

class Gravity(ForceGenerator):
    # Global Constants
    G: float = 6.67 * math.pow(10, -7) # Newton's Universal Gravitational Constant
    M_earth : float = 5.97 * math.pow(10, 24) # mass of planet earth
    g_earth : float = 9.8 # gravitational field strength of planet earth

    def __init__(self, gravitational_field_strength : float) -> None:
        self.gravitational_field_strength = gravitational_field_strength

    # get_force(self, particle : Particle) -> Vector
    # Returns the gravitational force acting upon the object
    def get_force(self, particle : Particle) -> Vector:
        return Vector(0, particle.mass * -self.gravitational_field_strength)
    
    def update_force(self, particle : Particle) -> None:
        particle.apply_force(self.get_force(particle))