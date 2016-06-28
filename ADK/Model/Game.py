from WelcomeScreen import WelcomeScreen
from ControlChoosing import ControlChoosing


class Game:

# PUBLIC METHODS

    def __init__(self, playArea, timer):
        self.state = WelcomeScreen()
        self.playArea = playArea
        self.timer = timer

    def NextState(self):
        self.state.NextState(self)

    def OnTimer(self):
        self.state.OnTimer()

    def KeyPressed(self, key):
        self.state.KeyPressed(key)

    def KeyReleased(self, key):
        self.state.KeyReleased(key)
        
    def GetStateName(self):
        return self.state.__class__.__name__
        
    # Intended for concrete states (WelcomeScreen, ControlChoosing, GameRound a FinalScoreBoard)
    def ChangeState(self, state):
        self.state = state
