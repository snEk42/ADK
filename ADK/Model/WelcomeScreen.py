from State import State
from ControlChoosing import ControlChoosing
from Player import Player


class WelcomeScreen(State):

# PUBLIC METHODS

    def NextState(self, game):
        players = self.CreatePlayers()
        game.ChangeState( ControlChoosing(players) )


# PRIVATE METHODS

    def CreatePlayers(self):
        # Colors of all six players (model representation)
        colors = ['red', 'yellow', 'orange', 'green', 'purple', 'blue']
        players = []
        for color in colors:
            player = Player(color)
            players.append(player)
        return players

