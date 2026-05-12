from python.physics.particle import Particle
from python.core.vector import Vector
import math

class Gravity:
    # Global Constants
    G: float = 6.67 * math.pow(10, -7) # Newton's Universal Gravitational Constant
    M_earth : float = 5.97 * math.pow(10, 24) # mass of planet earth
    g_earth : float = 9.8 # gravitational field strength of planet earth

    def get_force(self, particle : Particle) -> Vector:
        return Vector(particle.mass * self.g_earth, -math.pi / 2)
    