class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        equal = (self.x == other.x) and (self.y == other.y)
        return equal

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "x: " + `self.x` + ", y: " + `self.y`

    def Copy(self):
        new = self.__class__(self.x, self.y)
        return new
