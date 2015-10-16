from wx.lib.pubsub import Publisher as pub
import random

from State import State
from LineHead import LineHead
from Exceptions import CrashException


class GameRound(State):

    def __init__(self, players, playArea):
        self.players = players
        self.playArea = playArea
        self.targetScore = 10*self.PlayersPlaying() - 10
        # At the beginning of the round noone has crashed yet
        self.playersAlive = self.PlayersPlaying()
        self.GenerateLineHeadsForPlayers()
        self.progress = "roundInAction"
        pub.sendMessage("STATE CHANGED", {'state': self.__class__.__name__, 'scores': self.GetScores()})


    def StartGameRound(self, timer):
        self.timer = timer
        self.ShowPlayers()
        self.timer.Start(0.005)


    def NextState(self):
        if self.progress != "roundOver":
            return self
        elif self.GetMaxScore() < self.targetScore:
            self.playArea.Clear()
            self.PreparePlayersForNextRound()
            return self.__class__(self.players, self.playArea)
        else:
            from FinalScoreBoard import FinalScoreBoard
            return FinalScoreBoard(self.GetScores())


    def KeyPressed(self, key):
        if   key == 49:     self.players[0].TurnLeft()    # 1
        elif key == 81:     self.players[0].TurnRight()   # Q
        elif key == 308:    self.players[1].TurnLeft()    # L.Ctrl
        elif key == 307:    self.players[1].TurnRight()   # L.Alt
        elif key == 77:     self.players[2].TurnLeft()    # M
        elif key == 44:     self.players[2].TurnRight()   # ,
        elif key == 314:    self.players[3].TurnLeft()    # L.Arrow
        elif key == 317:    self.players[3].TurnRight()   # D.Arrow
        elif key == 392:    self.players[4].TurnLeft()    # /
        elif key == 387:    self.players[4].TurnRight()   # *
        elif key == 1:      self.players[5].TurnLeft()    # L.Mouse
        elif key == 2:      self.players[5].TurnRight()   # R.Mouse


    def KeyReleased(self, key):
        if   key == 49  or key == 81:     self.players[0].GoStraight()  # 1 Q
        elif key == 308 or key == 307:    self.players[1].GoStraight()  # L.Ctrl L.Alt
        elif key == 77  or key == 44:     self.players[2].GoStraight()  # M ,
        elif key == 314 or key == 317:    self.players[3].GoStraight()  # L.Arrow D.Arrow
        elif key == 392 or key == 387:    self.players[4].GoStraight()  # / *
        elif key == 1   or key == 2:      self.players[5].GoStraight()  # L.Mouse R.Mouse


    def OnTimer(self):
        self.MainLoop()


    def MainLoop(self):
        for player in self.players:
            if player.isPlaying and (not player.hasCrashed):
                self.SetRandomInvisibility(player)
                self.MovePlayer(player)


    def MovePlayer(self, player):
        try:
            player.Move()
        except CrashException as crash:
            player.hasCrashed = True
            self.playersAlive -= 1
            self.UpdateScores()
            if self.playersAlive < 2:
                self.progress = "roundOver"
                self.timer.Stop()


    def SetRandomInvisibility(self, player):
        random.seed()
        if random.randint(1, 800) == 42:
            player.TurnInvisible(random.randint(15, 25))


    def UpdateScores(self):
        scores = {}
        for player in self.players:
            if player.isPlaying:
                if not player.hasCrashed:
                    player.IncrementScore()
                color = player.color
                score = player.score
                scores[color] = score
        pub.sendMessage("SCORE CHANGED", scores)


    def GetScores(self):
        scores = {}
        for player in self.players:
            if player.isPlaying:
                color = player.color
                score = player.score
                scores[color] = score
        return scores


    def GetMaxScore(self):
        maxScore = 0
        for player in self.players:
            if player.isPlaying:
                if player.score > maxScore:
                    maxScore = player.score
        return maxScore


    def ShowPlayers(self):
        for player in self.players:
            if player.isPlaying:
                player.Blink()


    def GenerateLineHeadsForPlayers(self):
        for player in self.players:
            if player.isPlaying:
                lineHead = self.GetRandomLineHead(player.color)
                player.SetLineHead(lineHead)


    def GetRandomLineHead(self, color):
        position = self.playArea.GetRandomPosition()
        direction = self.playArea.GetRandomDirection()
        lineHead = LineHead(self.playArea, color, position, direction)
        return lineHead


    def PreparePlayersForNextRound(self):
        # In new round noone should start already as crashed
        for player in self.players:
            player.hasCrashed = False


    def PlayersPlaying(self):
        playing = 0
        for player in self.players:
            if player.isPlaying:
                playing += 1
        return playing
