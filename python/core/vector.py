from __future__ import annotations
import math

class Vector:
    def __init__(self, x : float, y : float) -> None:
        self.x = x
        self.y = y

    # Getters and Setters
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

    # Derived Properties
    @property
    def magnitude(self) -> float:
        return math.hypot(self.x, self.y)
    
    @property
    def angle(self) -> float:
        return math.atan2(self.y,self.x)

    # Vector Operations
    def add(self, other : Vector) -> Vector:
        x_components = self.x + other.x
        y_components = self.y + other.y

        return Vector(x_components, y_components)
    
    def multiply(self, scalar : float) -> Vector:
        return Vector(
            self.x * scalar,
            self.y * scalar
        )
    
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
    
    # Returns a unit vector
    def normalize(self) -> Vector:
        if self.magnitude == 0:
            raise ValueError("Cannot normalize a vector with magnitude of zero")
        
        return self.multiply(1 / self.magnitude)
    
    # Other Methods
    def copy(self) -> Vector:
        return Vector(self.x, self.y)
    
    # Vector Overloading 
    def __add__(self, other : Vector) -> Vector:
        return self.add(other)
    
    def __sub__(self, other : Vector) -> Vector:
        return self.subtract(other)
    
    def __mul__(self, scalar : float) -> Vector:
        return self.multiply(scalar)
    
    def __rmul__(self, scalar : float) -> Vector:
        return self.multiply(scalar)