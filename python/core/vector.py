from __future__ import annotations
import math

class Vector:
    def __init__(self, magnitude : float, angle : float):
        self.magnitude = magnitude
        self.angle = angle

    # Getter & Setter Methods
    def get_magnitude(self) -> float:
        return self.magnitude
    
    def get_angle(self) -> float:
        return self.angle
    
    def get_x(self) -> float:
        return self.magnitude * math.cos(self.angle)
    
    def get_y(self) -> float:
        return self.magnitude * math.sin(self.angle)

    def set_magnitude(self, magnitude : float) -> None:
        self.magnitude = magnitude

    def set_angle(self, angle : float) -> None:
        self.angle = angle
    
    # Vector Operations
    @staticmethod
    def calc_magnitude(x : float, y : float) -> float:
        return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

    def add(self, other : Vector) -> Vector:
        x_components = self.get_x() + other.get_x()
        y_components = self.get_y() + other.get_y()

        theta = math.atan(y_components / x_components)
        mag = self.calc_magnitude(x_components, y_components)

        return Vector(mag, theta)
    
    def multiply(self, other : float) -> Vector:
        x_component = self.get_x() * other
        y_component = self.get_y() * other

        mag = self.calc_magnitude(x_component, y_component)
        return Vector(mag, self.get_angle())
    
    def subtract(self, other : Vector) -> Vector:
        other = other.multiply(-1)
        return self.add(other)

    def dot_product(self, other : Vector) -> float:
        x_components = self.get_x() * other.get_x()
        y_components = self.get_y() * other.get_y()

        return x_components + y_components
    
    def angle_between(self, other : Vector) -> float:
        mags = self.get_magnitude() * other.get_magnitude()

        return math.acos(self.dot_product(other) / mags)
