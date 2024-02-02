import random
while True:
    list=['rock','paper','scissors']
    computer=random.choice(list)
    player=None
    while player not in list:
        player=(input('rock, paper or scissors: ')).lower()

    print('player:',player)
    print('computer:',computer)

    if player==computer:
        print('draw')
    elif player=='rock' and computer=='scissors':
        print('you win')
    elif player=='paper'and computer=='rock':
        print('you win')
    elif player=='rock'and computer=='paper':
        print('you lose')
    elif player=='paper'and computer=='scissors':
        print('you lose')
    elif player=='scissors'and computer=='rock':
        print('you lose')
    elif player=='scissors'and computer=='paper':
        print('you win')

    ch=input('do you want to continue? y/n :')
    if ch.lower()=='y' or ch.lower()=='yes':
        continue
    else:
        print('thank you for playing')
        break