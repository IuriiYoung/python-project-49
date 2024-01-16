#!/usr/bin/env python3

def procedure(game_num: int):
    import prompt
    name = prompt.string('May I have your name? ')
    print(f'Hello,{name}!')
    count = 0
    if game_num == 1:
        from games.game_calc import game
    elif game_num == 2:
        from games.game_even import game
    elif game_num == 3:
        from games.game_gsd import game
    elif game_num == 4:
        from games.game_progression import game
    else:
        print('wrong game type')
    while count < 4:
        if count == 3:
            print(f'Congratulations, {name}!')
            break
        elif game() is True:
            count = count + 1
        else:
            print(f"Wrong answer. Let's try again {name}!")
            break


def main():
    procedure()


if __name__ == '__main__':
    main()
