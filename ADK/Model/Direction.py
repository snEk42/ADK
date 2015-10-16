
class Direction:
    def __str__(self):
        return self.__class__.__name__

    def __eq__(self, other):
        equal = (self.__class__.__name__ == other.__name__)
        return equal

    def __ne__(self, other):
        return not self.__eq__(other)

    def __mul__(self, other):
        return self.integerRepresentation * other


class Left(Direction):
    integerRepresentation = 1


class Right(Direction):
    integerRepresentation = -1


class Straight(Direction):
    integerRepresentation = 0