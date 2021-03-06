import wx
from wx.lib.pubsub import pub

from Model.Game import Game
from View.View  import View


class Controller:

    # Control keys in order: (1 & Q), (L.Ctrl & L.Alt), (M & ,), (L.Arrow & D.Arrow), (/ & *)
    controlKeys = [49, 81, 308, 307, 77, 44, 314, 317, 392, 387]

    def __init__(self, app):
        self.view = View(None)
        self.BindKeyEvents(self.view)
        self.SubscribeModelSignals() # Must subscribe before Game is created, elsewise view wouldn't show welcome screen
        self.PrepareTimer()
        playArea = self.view.GetPlayArea()
        self.model = Game(playArea, self.timer)


    def BindKeyEvents(self, view):
        view.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        view.panel.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        view.panel.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
        view.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
        view.panel.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        view.panel.Bind(wx.EVT_RIGHT_UP, self.OnRightUp)


    def SubscribeModelSignals(self):
        pub.subscribe(self.OnStateChange, "STATE CHANGED")
        pub.subscribe(self.OnReadyChange, "READY CHANGED")
        pub.subscribe(self.OnScoreChange, "SCORE CHANGED")
        pub.subscribe(self.OnPlayAreaChange, "PLAYAREA CHANGED")


    def PrepareTimer(self):
        self.timer = wx.Timer(self.view)
        self.view.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)


    def OnTimer(self, event):
        self.model.OnTimer()


    def OnKeyDown(self, event):
        keyCode = event.GetKeyCode()
        if keyCode in self.controlKeys:
            self.model.KeyPressed(keyCode)
        elif keyCode == wx.WXK_SPACE:
            self.model.NextState()
        elif keyCode == wx.WXK_ESCAPE:
            if self.model.GetStateName() == "WelcomeScreen":
                self.view.Close() # Close whole application
            else:
                playArea = self.view.GetPlayArea()
                self.model = Game(playArea, self.timer)


    def OnKeyUp(self, event):
        keyCode = event.GetKeyCode()
        if keyCode in self.controlKeys:
            self.model.KeyReleased(keyCode)


    def OnLeftDown(self, event):
        self.model.KeyPressed(1)


    def OnLeftUp(self, event):
        self.model.KeyReleased(1)


    def OnRightDown(self, event):
        self.model.KeyPressed(2)


    def OnRightUp(self, event):
        self.model.KeyReleased(2)


    def OnStateChange(self, state, scores=None):
        if state == "WelcomeScreen":
            self.view.DisplayWelcomeScreen()
        elif state == "ControlChoosing":
            self.view.DisplayControlChoosing()
        elif state == "GameRound":
            self.view.DisplayGameRound(scores)
        elif state == "FinalScoreBoard":
            self.view.DisplayFinalScoreBoard(scores)


    def OnReadyChange(self, color, ready):
        self.view.DisplayReadyStatement(color, ready)


    def OnScoreChange(self, scores):
        self.view.DisplayNewScores(scores)


    def OnPlayAreaChange(self, color, points):
        self.view.DisplayPoints(color, points)


if __name__ == "__main__":
    app = wx.App(False)
    controller = Controller(app)
    app.MainLoop()
