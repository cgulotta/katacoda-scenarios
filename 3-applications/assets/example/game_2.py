def start_adventure():
    print('You enter a room with two doors, one red, one blue.')
    door = input('which do you choose?')

    if door == 'red':
        print('As you open the red door, a fiendish goblin springs to attack you!')
    elif door == 'blue':
        print('You walk through the blue door and find an open treasure chest glittering with gold coins')
    else:
        print('I'm afraid that's not an option.')
        start_adventure()

if __name__ == '__main__':
    player_name = input('whats your name? >')
    print(f"Your name is: {player_name}")
    start_adventure()