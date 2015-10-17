from wx.lib.pubsub import pub

from Direction import Left, Right, Straight

class Player:

    score = 0
    isPlaying = False
    hasCrashed = False
    turningDirection = Straight()

    def __init__(self, color):
        self.color = color


    def SetLineHead(self, lineHead):
        self.lineHead = lineHead


    def SetPlaying(self, value):
        if self.isPlaying != value:
            self.isPlaying = value
            pub.sendMessage("READY CHANGED", message={'color': self.color, 'ready': self.isPlaying})


    def IncrementScore(self):
        self.score += 1


    def TurnLeft(self):
        self.turningDirection = Left()


    def TurnRight(self):
        self.turningDirection = Right()


    def GoStraight(self):
        self.turningDirection = Straight()


    def TurnInvisible(self, cycles):
        self.lineHead.TurnInvisible(cycles)


    def Blink(self):
        self.lineHead.Blink(5) # Blink five times


    def Move(self):
        self.lineHead.MoveToNextPosition(self.turningDirection)
