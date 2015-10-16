from State import State
from ControlChoosing import ControlChoosing
from Player import Player


class WelcomeScreen(State):


    def NextState(self):
        players = self.CreatePlayers()
        return ControlChoosing(players)


    def CreatePlayers(self):
        # Colors of all six players (model representation)
        colors = ['red', 'yellow', 'orange', 'green', 'purple', 'blue']
        players = []
        for color in colors:
            player = Player(color)
            players.append(player)
        return players

