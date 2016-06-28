from State import State

class ControlChoosing(State):

# PUBLIC METHODS

    def __init__(self, players):
        State.__init__(self)
        self.players = players

    def NextState(self, game):
        if self.PlayersReady() > 1:
            from GameRound import GameRound
            game.ChangeState( GameRound(self.players, game.playArea, game.timer) )

    def KeyPressed(self, key):
        if key == 49:       self.players[0].SetPlaying(True)    # 1
        elif key == 81:     self.players[0].SetPlaying(False)   # Q
        elif key == 308:    self.players[1].SetPlaying(True)    # L.Ctrl
        elif key == 307:    self.players[1].SetPlaying(False)   # L.Alt
        elif key == 77:     self.players[2].SetPlaying(True)    # M
        elif key == 44:     self.players[2].SetPlaying(False)   # ,
        elif key == 314:    self.players[3].SetPlaying(True)    # L.Arrow
        elif key == 317:    self.players[3].SetPlaying(False)   # D.Arrow
        elif key == 392:    self.players[4].SetPlaying(True)    # /
        elif key == 387:    self.players[4].SetPlaying(False)   # *
        elif key == 1:      self.players[5].SetPlaying(True)    # L.Mouse
        elif key == 2:      self.players[5].SetPlaying(False)   # R.Mouse

# PRIVATE METHODS

    def PlayersReady(self):
        ready = 0
        for player in self.players:
            if player.isPlaying:
                ready += 1
        return ready
