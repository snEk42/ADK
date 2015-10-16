import random
from wx.lib.pubsub import Publisher as pub

from Point import Point
from Exceptions import CrashException


class PlayArea:

    def __init__(self, maxPoint, backgroundColor):
        self.maxPoint = maxPoint
        self.backgroundColor = backgroundColor
        self.colorHashes = {backgroundColor: 0, 'red': 1, 'yellow': 2, 'orange': 3, 'green': 4, 'purple': 5, 'blue': 6}
        self.grid = [[0]*maxPoint.x for i in range(maxPoint.y)]


    def Clear(self):
        del self.grid
        self.grid = [[0]*self.maxPoint.x for i in range(self.maxPoint.y)]


    def ColorPoints(self, color, points):
        if not self.PointsInRange(points):
            raise CrashException('Points out of playarea')
        for point in points:
            if self.grid[point.y][point.x] == 0:
                self.grid[point.y][point.x] = self.colorHashes[color]
            else:
                raise CrashException('Crash with other color')
        pub.sendMessage("PLAYAREA CHANGED", {'color': color, 'points': points})


    def ColorPointsForced(self, color, points):
        for point in points:
            self.grid[point.y][point.x] = self.colorHashes[color]
        pub.sendMessage("PLAYAREA CHANGED", {'color': color, 'points': points})


    def GetRandomPosition(self):
        random.seed()
        x = random.randint(100, self.maxPoint.x-101)
        y = random.randint(100, self.maxPoint.y-101)
        return Point(x,y)


    def GetRandomDirection(self):
        random.seed()
        direction = random.randint(0, 359)
        return direction


    def GetBackgroundColor(self):
        return self.backgroundColor


    def PointsInRange(self, points):
        for point in points:
            if not self.HasPoint(point):
                return False
        return True


    def HasPoint(self, point):
        if (point.x > -1) and (point.x < self.maxPoint.x):
            if (point.y > -1) and (point.y < self.maxPoint.y):
                return True
        return False