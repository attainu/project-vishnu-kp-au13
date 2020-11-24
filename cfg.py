grid_x = 10
grid_y = 10
players_tot = 0
player_names = []
players = []
currentPlayerIndex = 0
snake_tot = 0
ladder_tot = 0
snake_pos = []
ladder_pos = []
winner = -1
diceValue = -1

class Player:
    '''all player objects are objects of this class'''
    def __init__(self,name):
        self.name = name
        self.coinPosition = 0
        self.streak = 0