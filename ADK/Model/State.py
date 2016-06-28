from wx.lib.pubsub import pub

# Class contains common interface with default implementations for four constrete
# state classes - WelcomeScreen, ControlChoosing, GameRound, FinalScoreBoard
class State:

# PUBLIC METHODS

    # Default implementation, consider redefinition
    def __init__(self):
        pub.sendMessage("STATE CHANGED", state=self.__class__.__name__)

    # Abstract, must be redefined
    def NextState(self, game):
        pass

    # Default implementation, consider redefinition
    def KeyPressed(self, key):
        pass

    # Default implementation, consider redefinition
    def KeyReleased(self, key):
        pass

    # Default implementation, consider redefinition
    def OnTimer(self):
        pass
        
    # Common to string conversion
    def __str__(self):
        return self.__class__.__name__

    # Common comparator override
    def __eq__(self, other):
        equal = (self.__class__.__name__ == other.__name__)
        return equal

    def __ne__(self, other):
        return not self.__eq__(other)
