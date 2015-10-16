import sched, time
from math import sin, cos, tan, atan, atan2, degrees, radians, sqrt, pi

from PlayArea import PlayArea
from Direction import *
from Point import Point



class LineHead:

    def __init__(self, playArea, color, position, direction):
        self.playArea = playArea
        self.color = color
        self.position = position
        self.direction = direction
        self.auxiliaryPoint = position.Copy()
        self.lastTurningDirection = Straight()
        self.cyclesUntilVisible = 0
        self.radius = 45


    def MoveToNextPosition(self, turningDirection):
        if turningDirection == Straight:
            if self.lastTurningDirection != Straight:
                self.lastTurningDirection = Straight()
                self.auxiliaryPoint = self.position.Copy()
            self.MoveFromAuxiliaryPoint()
        else:
            if self.lastTurningDirection != turningDirection.__class__: # The turning direction has changed
                self.auxiliaryPoint = self.GetRotationCenter(turningDirection) # We need a new rotation center
                self.lastTurningDirection = turningDirection
            self.MoveAroundAuxiliaryPoint(turningDirection)


    def MoveAroundAuxiliaryPoint(self, turningDirection):
        # How can coordinates of current position possibly change
        possibleXMove = self.Sign(cos(radians(self.direction)))
        possibleYMove = self.Sign(sin(radians(self.direction)))
        # Count new position if x changed
        newXMovePosition = self.position.Copy()
        newXMovePosition.x += possibleXMove
        newXMovePositionDivergence = abs(self.radius - self.GetPointsDistance(newXMovePosition, self.auxiliaryPoint))
        # Count new position if y changed
        newYMovePosition = self.position.Copy()
        newYMovePosition.y += possibleYMove
        newYMovePositionDivergence = abs(self.radius - self.GetPointsDistance(newYMovePosition, self.auxiliaryPoint))
        # Set current position to less diverging new position
        # and set change variables for easy move direction determination
        xMove, yMove = (0, 0)
        if newXMovePositionDivergence <= newYMovePositionDivergence:
            self.position = newXMovePosition
            xMove = possibleXMove
        else:
            self.position = newYMovePosition
            yMove = possibleYMove
        self.UpdateDirection(turningDirection)
        # Finally update the playarea
        self.ShowNewPositionOnPlayArea(xMove, yMove)


    def MoveFromAuxiliaryPoint(self):
        if self.direction in [0, 90, 180, 270]:
            self.MoveInTrivialDirection()
            return
        # Prepare relative position for general formula use
        relPosition = self.position.Copy()
        relPosition.x -= self.auxiliaryPoint.x
        relPosition.y -= self.auxiliaryPoint.y
        # How can coordinates of current position possibly change
        possibleXMove = self.Sign(cos(radians(self.direction)))
        possibleYMove = self.Sign(sin(radians(self.direction)))
        # Prepare direction slope
        slope = tan(radians(self.direction))
        # Count new position if x changed
        newXMovePosition = relPosition.Copy()
        newXMovePosition.x += possibleXMove
        newXMovePositionDivergence = abs(slope*newXMovePosition.x - newXMovePosition.y) / sqrt(slope**2 + 1)
        # Count new position if y changed
        newYMovePosition = relPosition.Copy()
        newYMovePosition.y += possibleYMove
        newYMovePositionDivergence = abs(slope*newYMovePosition.x - newYMovePosition.y) / sqrt(slope**2 + 1)
        # Set current position to less diverging new position
        # and set change variables for easy move direction determination
        xMove, yMove = (0, 0)
        if newXMovePositionDivergence <= newYMovePositionDivergence:
            self.position = newXMovePosition
            xMove = possibleXMove
        else:
            self.position = newYMovePosition
            yMove = possibleYMove
        # Set the position back to absolute value
        self.position.y += self.auxiliaryPoint.y
        self.position.x += self.auxiliaryPoint.x
        # Finally update the playarea
        self.ShowNewPositionOnPlayArea(xMove, yMove)


    def GetRotationCenter(self, turningDirection):
        if self.direction in [0, 180]:
            return self.GetRotationCenterForTrivialDirections(turningDirection)
        rotationCenter = self.position.Copy()
        if turningDirection == Left:
            tangentAngle = radians(self.direction) + (pi/2) # In radians
        else:
            tangentAngle = radians(self.direction) - (pi/2) # In radians
        tangentSlope = tan(tangentAngle)
        x = self.radius / sqrt(1 + tangentSlope**2)
        y = tangentSlope * x
        xSign = self.Sign(cos(tangentAngle))
        ySign = self.Sign(sin(tangentAngle))
        rotationCenter.x += xSign * self.Round(x)
        rotationCenter.y += ySign * self.Round(abs(y))
        return rotationCenter


    def MoveInTrivialDirection(self):
        xMove, yMove = (0, 0)
        if self.direction == 90:
            self.position.y += 1
            yMove = 1
        elif self.direction == 270:
            self.position.y -= 1
            yMove = -1
        elif self.direction == 0:
            self.position.x += 1
            xMove = 1
        elif self.direction == 180:
            self.position.x -= 1
            xMove = -1
        self.ShowNewPositionOnPlayArea(xMove, yMove)


    def GetRotationCenterForTrivialDirections(self, turningDirection):
        rotationCenter = self.position.Copy()
        if self.direction == 0:
            if turningDirection == Left:
                rotationCenter.y += self.radius
            else:
                rotationCenter.y -= self.radius
        elif self.direction == 180:
            if turningDirection == Left:
                rotationCenter.y -= self.radius
            else:
                rotationCenter.y += self.radius
        return rotationCenter


    def UpdateTrivialDirections(self, a, b):
        if (b == 0):
            if self.direction in range(160, 200):
                self.direction = 180
            elif (self.direction in range(0, 20)) or (self.direction in range(340, 380)):
                self.direction = 0
            return
        elif (a == 0):
            if self.direction in range(250, 290):
                self.direction = 270
            elif self.direction in range(70, 110):
                self.direction = 90
            return


    def UpdateDirection(self, turningDirection):
        a = self.position.y - self.auxiliaryPoint.y
        b = self.position.x - self.auxiliaryPoint.x
        if (a == 0) or (b == 0):
            self.UpdateTrivialDirections(a, b)
            return

        if (a > 0) and (b > 0):
            parcialAngle = self.Round( degrees(atan(abs(float(a))/abs(b))) )
            self.direction = (parcialAngle + 90) % 360
        elif (a > 0) and (b < 0):
            parcialAngle = self.Round( degrees(atan(abs(float(b))/abs(a))) )
            self.direction = (parcialAngle + 180) % 360
        elif (a < 0) and (b < 0):
            parcialAngle = self.Round( degrees(atan(abs(float(a))/abs(b))) )
            self.direction = (parcialAngle + 270) % 360
        else:
            parcialAngle = self.Round( degrees(atan(abs(float(b))/abs(a))) )
            self.direction = self.Round( degrees(atan(abs(float(b))/abs(a))) )

        if turningDirection == Right:
            self.direction = (self.direction - 180) % 360


    def GetPointsDistance(self, point1, point2):
        a2 = (point1.x - point2.x)**2
        b2 = (point1.y - point2.y)**2
        return sqrt(a2+b2)


    def ShowNewPositionOnPlayArea(self, xMove, yMove):
        if self.cyclesUntilVisible > 0:
            self.cyclesUntilVisible -= 1
            return
        points = []
        if yMove != 0:
            y = self.position.y + yMove
            for x in range(-1, 2):
                new = Point(self.position.x + x, y)
                points.append(new)
        elif xMove != 0: # Should be everytime if first condition was false
            x = self.position.x + xMove
            for y in range(-1, 2):
                new = Point(x, self.position.y + y)
                points.append(new)
        self.playArea.ColorPoints(self.color, points)


    def TurnInvisible(self, cycles):
        self.cyclesUntilVisible = cycles


    def Blink(self, numberOfTimes):
        s = sched.scheduler(time.time, time.sleep)
        headPoints = self.GetHeadPoints()
        for x in range(0, numberOfTimes):
            s.enter(0.1, 1, self.ColorHead, argument=(self.color, headPoints))
            s.enter(0.2, 1, self.ColorHead, argument=('black', headPoints))
            s.run()
        # I wan't the line head to stay displayed after blinking
        self.ColorHead(self.color, headPoints)


    def ColorHead(self, color, headPoints):
        self.playArea.ColorPointsForced(color, headPoints)


    def GetHeadPoints(self):
        points = []
        middleX = self.position.x
        middleY = self.position.y
        for x in range(middleX - 1, middleX + 2):
            for y in range(middleY - 1, middleY + 2):
                newPoint = Point(x, y)
                points.append(newPoint)
        return points


    def Sign(self, number):
        if number >= 0: # I'm an optimist :-)
            return 1
        else:
            return -1


    def Round(self, number):
        if (number > 0):
            return int(number + .5)
        else:
            return int(number - .5)
