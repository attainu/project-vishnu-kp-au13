import cfg
import random
import sys


def getInputs():
    cfg.snake_tot = int(input("Enter number of snakes: "))
    i = 1
    while(i <= cfg.snake_tot):
        snake_pos = input()
        position_tuple = tuple(int(x) for x in snake_pos.split(" "))
        if(position_tuple[0] < position_tuple[1]):
            print("Oops. Head of snake below tail of snake. Exiting...")
            sys.exit()
        cfg.snake_pos.append(position_tuple)
        i = i+1

    cfg.ladder_tot = int(input("Enter number of ladders: "))
    i = 1
    while(i <= cfg.ladder_tot):
        ladder_pos = input()
        position_tuple = tuple(int(x) for x in ladder_pos.split(" "))
        if(position_tuple[0] > position_tuple[1]):
            print("Oops. Start of ladder above end of ladder. Exiting...")
            sys.exit()
        cfg.ladder_pos.append(position_tuple)
        i = i+1

    cfg.players_tot = int(input("Enter number of players: "))
    i = 1
    while(i <= cfg.players_tot):
        name = input()
        cfg.player_names.append(name)
        obj = cfg.Player(name)
        cfg.players.append(obj)
        i = i+1

def displayInputs():
    print(cfg.ladder_pos, cfg.snake_pos, cfg.player_names)

def checkForWinner(player):
    if(player.coinPosition > (cfg.grid_x * cfg.grid_y)):
        player.coinPosition -= cfg.diceValue
    if(player.coinPosition == (cfg.grid_x * cfg.grid_y)):
        cfg.winner = player.name
        print(player.name, "has rolled a", cfg.diceValue, "and moved from", player.coinPosition - cfg.diceValue, "to", player.coinPosition)
        print(player.name, "has won the game")
        sys.exit()




