import wx


class GamePanel(wx.Panel):

    colors = {'red': '#FF2800', 'yellow': '#C3C300', 'orange': '#FF7900', 'green': '#00CB00', 'purple': '#DF51B6', 'blue': '#00A2CB', 'black': '#000000'}

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.sizer = wx.BoxSizer()
        self.panel = wx.Panel(self)
        self.sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)


    def ShowWelcomeImage(self):
        self.ClearPanel()
        dc = wx.ClientDC(self.panel)
        welcomeImage = wx.Bitmap("View\\Achtung.jpg")
        (x, y) = self.panel.GetSize()
        (ix, iy) = welcomeImage.GetSize()
        dc.DrawBitmap(welcomeImage, (x-ix)/2, (y-iy)/2, True)


    def DisplayControlChoosing(self):
        self.ClearPanel()
        self.DisplayControlOptions()
        self.AddEventHandlersOnNewElements()


    def DisplayControlOptions(self):
        dc = wx.ClientDC(self.panel)
        playerColors = self.colors.keys()
        playerColors.remove('black')
        for color in playerColors:
            (x, y) = self.GetReadyCoordinates(color)
            controlOption = wx.Bitmap("View\\Controls\\%s.gif" % (color.title()))
            controlOptionWidth = controlOption.GetWidth()
            dc.DrawBitmap(controlOption, x-controlOptionWidth, y, True)


    def DisplayFinalScoreBoard(self, scores):
        self.ClearPanel()
        self.ShowEndOfGame()
        self.DisplayFinalScore(scores)
        self.AddEventHandlersOnNewElements()


    def DisplayReadyStatement(self, color, ready):
        dc = wx.ClientDC(self.panel)
        (x, y) = self.GetReadyCoordinates(color)
        if ready == True:
            ready = wx.Bitmap("View\\Readys\\%s.gif" % (color.title()))
        else:
            ready = wx.Bitmap("View\\Readys\\Blank.gif")
        dc.DrawBitmap(ready, x, y, True)
        self.AddEventHandlersOnNewElements()


    def DisplayGameRoundTemplate(self, scores):
        self.ClearPanel()
        self.DisplayRoundBackground()
        self.DisplayScoresInRound(scores)
        self.AddEventHandlersOnNewElements()


    def AddEventHandlersOnNewElements(self):
        for child in self.GetChildren():
            child.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
            child.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
            child.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
            child.Bind(wx.EVT_RIGHT_UP, self.OnRightUp)
            for subchild in child.GetChildren():
                subchild.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
                subchild.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
                subchild.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
                subchild.Bind(wx.EVT_RIGHT_UP, self.OnRightUp)


    def DisplayScoresInRound(self, scores):
        dc = wx.ClientDC(self.panel)
        for color in scores:
            (x, y) = self.GetScoreCoordinates(color)
            if scores[color] < 10:
                score = wx.Bitmap("View\\Scores\\%s\\%i.gif" % (color, scores[color]))
                dc.DrawBitmap(score, x, y, True)
            else:
                score10 = wx.Bitmap("View\\Scores\\%s\\%i.gif" % (color, scores[color]/10))
                score1 = wx.Bitmap("View\\Scores\\%s\\%i.gif" % (color, scores[color]%10))
                scoreWidth = score10.GetWidth()
                dc.DrawBitmap(score10, x, y, True)
                dc.DrawBitmap(score1, x+scoreWidth+1, y, True)


    def DisplayFinalScore(self, scores):
        dc = wx.ClientDC(self.panel)
        for color in scores:
            (x, y) = self.GetFinalScoreCoordinates(color)
            if scores[color] < 10:
                score = wx.Bitmap("View\\FinalScores\\%s\\%i.gif" % (color, scores[color]))
                dc.DrawBitmap(score, x, y, True)
            else:
                score10 = wx.Bitmap("View\\FinalScores\\%s\\%i.gif" % (color, scores[color] / 10))
                score1 = wx.Bitmap("View\\FinalScores\\%s\\%i.gif" % (color, scores[color] % 10))
                scoreWidth = score10.GetWidth()
                dc.DrawBitmap(score10, x, y, True)
                dc.DrawBitmap(score1, x + scoreWidth + 4, y, True)


    def ShowEndOfGame(self):
        dc = wx.ClientDC(self.panel)
        welcomeImage = wx.Bitmap("View\\End.gif")
        (x, y) = self.panel.GetSize()
        (ix, iy) = welcomeImage.GetSize()
        dc.DrawBitmap(welcomeImage, (x - ix) / 2, (y - iy - 50), True)


    def GetScoreCoordinates(self, color):
        (x, y) = self.panel.GetSize()
        y0 = (y - 408)/2 * 5/10
        x0 = (x - 100)
        if color == 'red':
            return (x0, y0)
        elif color == 'yellow':
            return (x0, y0+73)
        elif color == 'orange':
            return (x0, y0+(2*73))
        elif color == 'green':
            return (x0, y0 + (3*73))
        elif color == 'purple':
            return (x0, y0 + (4*73))
        elif color == 'blue':
            return (x0, y0 + (5*73))


    def GetFinalScoreCoordinates(self, color):
        (x, y) = self.panel.GetSize()
        y0 = (y - 400) / 2 * 6 / 10
        x0 = (x - 300) / 2
        if color == 'red':
            return (x0, y0)
        elif color == 'yellow':
            return (x0, y0 + 60)
        elif color == 'orange':
            return (x0, y0 + (2 * 60))
        elif color == 'green':
            return (x0, y0 + (3 * 60))
        elif color == 'purple':
            return (x0, y0 + (4 * 60))
        elif color == 'blue':
            return (x0, y0 + (5 * 60))


    def GetReadyCoordinates(self, color):
        (x, y) = self.panel.GetSize()
        y0 = (y - 408) / 2 * 8 / 10
        x0 = (x - 100) / 2
        if color == 'red':
            return (x0, y0)
        elif color == 'yellow':
            return (x0, y0 + 73)
        elif color == 'orange':
            return (x0, y0 + (2 * 73))
        elif color == 'green':
            return (x0, y0 + (3 * 73))
        elif color == 'purple':
            return (x0, y0 + (4 * 73))
        elif color == 'blue':
            return (x0, y0 + (5 * 73))


    def DisplayRoundBackground(self):
        dc = wx.ClientDC(self.panel)
        background = wx.Bitmap('View\\Scores\\Background.gif')
        (iw, ih) = background.GetSize()
        (x, y) = self.panel.GetSize()
        for i in range(0, y, ih):
            dc.DrawBitmap(background, x-iw, i, True)


    def ClearPanel(self):
        newpanel = wx.Panel(self)
        self.sizer.Replace(self.panel, newpanel)
        self.panel.Destroy()
        self.panel = newpanel
        self.Layout()


    def DisplayPoints(self, color, points):
        (x, y) = self.panel.GetSize()
        dc = wx.ClientDC(self.panel)
        dc.SetPen(wx.Pen(self.colors[color], 1))
        for point in points:
            dc.DrawPoint(point.x, y - point.y)


    def OnLeftDown(self, event):
        wx.PostEvent(self, event)


    def OnLeftUp(self, event):
        wx.PostEvent(self, event)


    def OnRightDown(self, event):
        wx.PostEvent(self, event)


    def OnRightUp(self, event):
        wx.PostEvent(self, event)
