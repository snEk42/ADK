from WelcomeScreen import WelcomeScreen
from ControlChoosing import ControlChoosing


class Game:

    def __init__(self, playArea):
        self.state = WelcomeScreen()
        self.playArea = playArea


    def NextState(self):
        # If state is going to change to main playing phase,
        # state has to have access to the play area.
        if self.state == ControlChoosing:
            self.state = self.state.NextState(self.playArea)
        # If anything else, just change the state, when it's possible.
        else:
            self.state = self.state.NextState()


    def KeyPressed(self, key):
        self.state.KeyPressed(key)


    def KeyReleased(self, key):
        self.state.KeyReleased(key)


    def GetState(self):
        return self.state.__class__.__name__
