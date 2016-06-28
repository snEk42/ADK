from wx.lib.pubsub import pub

from State import State
from WelcomeScreen import WelcomeScreen

class FinalScoreBoard(State):

# PUBLIC METHODS

    def __init__(self, scores):
        self.scores = scores
        pub.sendMessage("STATE CHANGED", state=self.__class__.__name__, scores=scores)

    def NextState(self, game):
        game.ChangeState( WelcomeScreen() )
