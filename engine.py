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

def doMove(playerId):
    cfg.diceValue = random.randint(1, 6)
    initialPosition = cfg.players[playerId].coinPosition
    cfg.players[playerId].coinPosition += cfg.diceValue
    checkForWinner(cfg.players[playerId])
    print(cfg.players[playerId].name, "has rolled a",
          cfg.diceValue, "and moved from", initialPosition, "to", cfg.players[playerId].coinPosition)
    for snakeCoord in cfg.snake_pos:
        if(snakeCoord[0] == cfg.players[playerId].coinPosition):
            print("Oh no! a wild snake at",
                  snakeCoord[0], 'bit', cfg.players[playerId].name)
            cfg.players[playerId].coinPosition = snakeCoord[1]
            print(cfg.players[playerId].name, "drops to", snakeCoord[1])
            return
    for ladderCoord in cfg.ladder_pos:
        if(ladderCoord[0] == cfg.players[playerId].coinPosition):
            print(cfg.players[playerId].name,
                  "has found a ladder and advances to", ladderCoord[1])
            cfg.players[playerId].coinPosition = ladderCoord[1]
            return





