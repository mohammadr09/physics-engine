from python.physics.forces.force import ForceGenerator
from python.physics.particle import Particle
from python.core.vector import Vector

class Drag(ForceGenerator):
    # Fd = 0.5 * pv^2DA
    def __init__(self, density : float, drag_coeff : float, area : float) -> None:
        self.density = density
        self.drag_coeff = drag_coeff
        self.area = area # cross-sectional area

    def get_force(self, particle: Particle) -> Vector:
        velocity : Vector = particle.velocity

        speed : float = velocity.magnitude

        if speed == 0:
            return Vector(0,0)
        
        drag_magnitude : float = (
            0.5
            * self.density
            * speed * speed
            * self.drag_coeff
            * self.area
        )

        drag_direction : Vector = velocity.normalize() * -1
        f_d : Vector = drag_direction * drag_magnitude

        return f_d
    
    def update_force(self, particle: Particle) -> None:
        particle.apply_force(self.get_force(particle))