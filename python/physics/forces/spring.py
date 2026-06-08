from python.physics.forces.force import ForceGenerator
from python.physics.particle import Particle
from python.core.vector import Vector

class Spring(ForceGenerator):
    # Fsp = kx
    def __init__(self, 
                 anchor : Vector,
                 k : float,
                 eq_length : float) -> None:
        self.anchor = anchor
        self.k = k
        self.eq_length = eq_length # equillibrium (rest) length of the spring

    # Getters and Setters
    @property
    def k(self) -> float:
        return self._k
    
    @k.setter
    def k(self, k : float) -> None:
        self._k = k

    @property
    def anchor(self) -> Vector:
        return self._anchor
    
    @anchor.setter
    def anchor(self, anchor_pos : Vector) -> None:
        self._anchor = anchor_pos

    @property
    def eq_length(self) -> float:
        return self._eq_length
    
    @eq_length.setter
    def eq_length(self, eq_length : float) -> None:
        self._eq_length = eq_length

    # Spring Force Methods
    def get_force(self, particle: Particle) -> Vector:
        displacement : Vector = particle.pos - self.anchor
        spring_length : float = displacement.magnitude

        if spring_length == 0:
            return Vector(0,0)
        
        # calculate the displacement of the spring
        x : float = spring_length - self.eq_length

        # Hooke's Law
        f_sp_magnitude : float = -self.k * x

        direction : Vector = displacement.normalize()
        
        return f_sp_magnitude * direction
    
    def update_force(self, particle: Particle) -> None:
        particle.apply_force(self.get_force(particle))
