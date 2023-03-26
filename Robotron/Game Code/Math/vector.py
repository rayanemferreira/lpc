from math import sqrt, atan


class Vector:
    """
    This is a 2D vector which is being used to define movement and all direc tional aspects in the game.
    This is one of the largest refactors in my code at this stage, and is designed to simplify to code.


    Why not use NumPy?
    Numpy is heavy, and the vector class, whilst feature rich, is too heavy for me. I want fast execution that
    is best achieved this way. I dont need the cross product, and other mathmatical opperations, as these are
    fairly simple movement vectors.
    """

    def __init__(self, i, j):
        # Basic i,j notation for vectors
        self.i = i
        self.j = j
        # Other defining charactaristics. mag is the length or magnitude, arg is the angle formed
        self.mag = sqrt(i ** 2 + j ** 2)
        if i:
            self.arg = atan(j / i)
        else:
            self.arg = 0
        # The unit vector for this vector
        if self.mag:
            self.ui = i / self.mag
            self.uj = j / self.mag
        else:
            self.ui = 0
            self.uj = 0

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.i + other.i, self.j + other.j)

    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.i - other.i, self.j - other.j)

    def __mul__(self, other: int) -> 'Vector':
        return Vector(self.i * other, self.j * other)

    def __truediv__(self, other: int) -> 'Vector':
        return Vector(self.i / other, self.j / other)

    def __iter__(self):
        yield self.i
        yield self.j

    def __str__(self):
        return f"Vector : ({self.i},{self.j}) - [mag:{self.mag}]"


