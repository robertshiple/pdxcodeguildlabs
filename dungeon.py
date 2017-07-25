import random
import time

class Player:
    
    def __init__(self, name, location_i, location_j):
        self.name = name
        self.location_i = location_i
        self.location_j = location_j
        self.health = 5


def print_board(board, player):
    for j in range(len(board)):
        for i in range(len(board[j])):
            if player.location_i == i and player.location_j == j:
                print('💩', end=' ')
            else:
                print(board[i][j], end=' ')
        print()


width = 10
height = 10
board = [[0 for j in range(height)] for i in range(width)]
player = Player('person', 0, 0)

for k in range(5):
    i = random.randint(0, width-1)
    j = random.randint(0, height-1)
    board[i][j] = '💀'

for k in range(1):
    i = random.randint(0, width-1)
    j = random.randint(0, height-1)
    board[i][j] = '🏛'

def check_location(board, player):
    if board[player.location_i][player.location_j] == '🏛':
        print('you win')
        exit()
    if board[player.location_i][player.location_j] == '💀':
        print('You have encountered happiness!')
        action = input('what do you do? ')
        if action == 'attack':
            print('You have ended your happiness!')
            board[player.location_i][player.location_j] = 0
        else:
            print('you are hurt. you have lost a health.')
            player.health = player.health - 1
            print(player.health)
        if player.health == 0:
            print('you dead!')
            exit()


while True:
    command = input('> ')
    if command == 'print':
        print_board(board, player)
    elif command == 'quit' or command == 'exit':
        print('goodbye')
        break
    elif command == 'n':
        if player.location_j > 0:
            player.location_j -= 1
            check_location(board, player)
        else:
            print('you can\'t move there')
        print_board(board, player)
    elif command == 's':
        if player.location_j < height-1:
            player.location_j += 1
            check_location(board, player)
        else:
            print('you can\'t move there')
        print_board(board, player)
    elif command == 'e':
        if player.location_i < width-1:
            player.location_i += 1
            check_location(board, player)
        else:
            print('you can\'t move there')
        print_board(board, player)
    elif command == 'w':
        if player.location_i > 0:
            player.location_i -= 1
            check_location(board, player)
        else:
            print('you can\'t move there')
        print_board(board, player)
    else:
        print('I did not recognize that command')