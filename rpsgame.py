import random

item_list = ['Rock', 'Paper', 'Scissor']

com_player = random.choice(item_list).lower()

player = input('enter your choice: Rock, Paper, Scissor, Quit').lower()

if player == com_player:
    print('Tie')

elif player == 'rock' and com_player == 'paper':
    print(com_player)
    print('com win')

elif player == 'rock' and com_player == 'scissor':
    print(com_player)
    print('player win')

elif player == 'paper' and com_player == 'rock':
    print(com_player)
    print('player win')

elif player == 'paper' and com_player == 'scissor':
    print(com_player)
    print('com win')

elif player == 'scissor' and com_player == 'rock':
    print(com_player)
    print('com win')

elif player == 'scissor' and com_player == "paper":
    print(com_player)
    print('player win')

elif player == 'quit':
    quit()

else:
    print('invalid input')
