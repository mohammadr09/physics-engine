from __future__ import annotations
import math

class Vector:
    def __init__(self, magnitude : float, angle : float) -> None:
        self.magnitude = magnitude
        self.angle = angle

    # Getter & Setter Methods   
    @property
    def magnitude(self) -> float:
        return self._magnitude
    
    @magnitude.setter
    def magnitude(self, magnitude : float) -> None:
        self._magnitude = magnitude

    @property
    def angle(self) -> float:
        return self._angle 
    
    @angle.setter
    def angle(self, angle : float) -> None:
        self._angle = angle 

    @property
    def x(self) -> float:
        return self._x 
    
    @x.setter
    def x(self, x : float) -> None:
        self._x = x 

    @property
    def y(self) -> float:
        return self._y
    
    @y.setter
    def y(self, y : float) -> None:
        self._y = y

    # Vector Operations
    @staticmethod
    def calc_magnitude(x : float, y : float) -> float:
        return math.hypot(x, y)
    
    @staticmethod
    def from_components(x : float, y : float) -> Vector:
        mag = math.hypot(x, y)
        angle = math.atan2(y, x)
        return Vector(mag, angle)
    
    def add(self, other : Vector) -> Vector:
        x_components = self.x + other.x
        y_components = self.y + other.y

        theta = math.atan2(y_components, x_components)
        mag = self.calc_magnitude(x_components, y_components)

        return Vector(mag, theta)
    
    def multiply(self, scalar : float) -> Vector:
        mag = abs(self.magnitude * scalar)
        angle = self.angle

        if scalar < 0:
            angle += math.pi

        return Vector(mag, angle)
    
    def subtract(self, other : Vector) -> Vector:
        other = other.multiply(-1)
        return self.add(other)

    def dot_product(self, other : Vector) -> float:
        x_components = self.x * other.x
        y_components = self.y * other.y

        return x_components + y_components
    
    def angle_between(self, other : Vector) -> float:
        mags = self.magnitude * other.magnitude

        if mags == 0:
            raise ValueError("Cannot compute angle with zero vector")
        
        cos_theta = self.dot_product(other) / mags
        cos_theta = max(-1, min(1, cos_theta)) # clamp

        return math.acos(cos_theta)
