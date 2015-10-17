from wx.lib.pubsub import pub

from State import State

class FinalScoreBoard(State):

    def __init__(self, scores):
        self.scores = scores
        pub.sendMessage("STATE CHANGED", message={'state': self.__class__.__name__, 'scores': scores})

    def NextState(self):
        from WelcomeScreen import WelcomeScreen
        return WelcomeScreen()
