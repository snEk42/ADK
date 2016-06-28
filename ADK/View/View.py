import wx

from GamePanel import GamePanel
from Model.PlayArea import PlayArea
from Model.Point import Point


class View(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title='Achtung Die Kurve! Revival', style=wx.CLOSE_BOX | wx.STAY_ON_TOP)
        self.panel = GamePanel(self)
        # Hide cursor
        cursor = wx.StockCursor(wx.CURSOR_BLANK)
        self.SetCursor(cursor)
        # Format the frame / window
        self.SetBackgroundColour(wx.BLACK)
        self.ShowFullScreen(True)
        self.Show()
        self.SetFocus()


    def GetPlayArea(self):
        (x, y) = self.panel.GetSize()
        return PlayArea(Point(x-140, y), 'black') # 140 is the score panel width


    def DisplayWelcomeScreen(self):
        self.panel.ShowWelcomeImage()


    def DisplayControlChoosing(self):
        self.panel.DisplayControlChoosing()


    def DisplayGameRound(self, scores):
        self.panel.DisplayGameRoundTemplate(scores)


    def DisplayFinalScoreBoard(self, scores):
        self.panel.DisplayFinalScoreBoard(scores)


    def DisplayPoints(self, color, points):
        self.panel.DisplayPoints(color, points)


    def DisplayNewScores(self, scores):
        self.panel.DisplayScoresInRound(scores)


    def DisplayReadyStatement(self, color, ready):
        self.panel.DisplayReadyStatement(color, ready)
