from __future__ import annotations
from python.core.vector import Vector
import random

class Particle:
    def __init__(self, pos : Vector,
                    velocity : Vector,
                    acceleration : Vector,
                    mass : float,
                    force : Vector | None = None
                 ) -> None:
        self.pos = pos
        self.velocity = velocity
        self.acceleration = acceleration
        self.mass = mass
        self.force = force if force is not None else Vector(0,0)
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    # Getters and Setters
    @property
    def mass(self) -> float:
        return self._mass
    
    @mass.setter
    def mass(self, value : float) -> None:
        if value <= 0:
            raise ValueError("Mass must be positive")
        
        self._mass = value

    @property
    def kinetic_energy(self) -> float:
        return 0.5 * self.mass * self.velocity.magnitude ** 2

    # apply_force(self, force) -> Vector
    #   To apply forces, we simply take the sum of the vectors.
    # This function is used to apply a specific force on the object.
    def apply_force(self, force : Vector) -> Vector:
        self.force = self.force.add(force)
        return self.force

    # apply(self) -> None
    #   (1) Using Newton's Second Law, F = ma, rearranging the equation yields: a = F/m.
    #   Using this, we can determine the particle's net acceleration by dividng F with
    #   the mass. We can also use this to update our velocity.
    #   (2) Since v = ∆d/∆t, to calculate our displacement (i.e., position),
    #   ∆d = v * ∆t. 
    #   (3) In real-life, Fnet does not continuously accumulate over change in time.
    #   Rather, the Fnet itself changes / is recalculated as time changes. Hence, we
    #   reset our force to (0, 0) at the end of the function.
    # This method applies all the forces acting upon the particle and recalculates
    # position, velocity, and acceleration.
    def apply(self, dt : float) -> None:
        self.acceleration = self.force.multiply(1 / self.mass)

        self.velocity = self.velocity.add(self.acceleration.multiply(dt))
        self.pos = self.pos.add(self.velocity.multiply(dt))

        self.force = Vector(0, 0)

