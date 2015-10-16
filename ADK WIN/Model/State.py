from wx.lib.pubsub import Publisher as pub


class State:

    def __init__(self):
        pub.sendMessage("STATE CHANGED", {"state": self.__class__.__name__})

    def __str__(self):
        return self.__class__.__name__

    def __eq__(self, other):
        equal = (self.__class__.__name__ == other.__name__)
        return equal

    def __ne__(self, other):
        return not self.__eq__(other)

    def NextState(self):
        pass

    def KeyPressed(self, key):
        pass

    def KeyReleased(self, key):
        pass

    def OnTimer(self):
        pass
