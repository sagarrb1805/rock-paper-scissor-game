import random

item_list = ['Rock', 'Paper', 'Scissor']

com_point = 0
player_point = 0

while True:
    com_player = random.choice(item_list).lower()

    player = input(' \n enter your choice: Rock, Paper, Scissor, Quit: ').lower()

    if player == com_player:
        print(' Tie')
        print(' Point table: \n Computer:{}  Player:{}'.format(com_point, player_point))

    elif player == 'rock' and com_player == 'paper':
        print('', com_player)
        print(' com win')
        com_point += 1
        print(' Point table: \n Computer:{}  Player:{}'.format(com_point, player_point))

    elif player == 'rock' and com_player == 'scissor':
        print('', com_player)
        print(' player win')
        player_point += 1
        print(' Point table: \n Computer:{}  Player:{}'.format(com_point, player_point))

    elif player == 'paper' and com_player == 'rock':
        print('', com_player)
        print(' player win')
        player_point += 1
        print(' Point table: \n Computer:{}  Player:{}'.format(com_point, player_point))

    elif player == 'paper' and com_player == 'scissor':
        print('', com_player)
        print(' com win')
        com_point += 1
        print(' Point table: \n Computer:{}  Player:{}'.format(com_point, player_point))

    elif player == 'scissor' and com_player == 'rock':
        print('', com_player)
        print(' com win')
        com_point += 1
        print(' Point table: \n Computer:{}  Player:{}'.format(com_point, player_point))

    elif player == 'scissor' and com_player == "paper":
        print('', com_player)
        print(' player win')
        player_point += 1
        print(' Point table: \n Computer:{}  Player:{}'.format(com_point, player_point))

    elif player == 'quit':
        quit()

    else:
        print(' invalid input')
