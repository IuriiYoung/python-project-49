#!/usr/bin/env python3

def start_calc():
    from games.game_calc import game
    from brain_games.game_seq import procedure
    procedure(1)

def main():
    start_calc()

if __name__ == '__main__':
    main()

