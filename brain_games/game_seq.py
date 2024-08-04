#!/usr/bin/env python3

def play_game(game):
    import prompt
    import importlib
    module = importlib.import_module(".".join(("brain_games", "games", game)))
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(module.DESCRIPTION)
    correct_answers = 0

    while correct_answers < 3:
        question, correct_answer = module.create_game()

        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # NOQA
            print(f"Let's try again, {name}!")
            break

    if correct_answers == 3:
        print(f"Congratulations, {name}!")


def main():
    play_game()


if __name__ == '__main__':
    main()
