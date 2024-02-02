#!/usr/bin/env python3

def play_game(game_name):
    import importlib
    chosen_game = importlib.import_module("brain_games.games.%s" % game_name)
    import prompt
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    count = 0
    while count < 4:
        if count == 3:
            print(f'Congratulations, {name}!')
            break
        elif chosen_game.play() == True:
            count = count + 1
        else:
            print(f"Let's try again {name}!")
            break

def main():
    play_game(game_name)


if __name__ == '__main__':
    main()


