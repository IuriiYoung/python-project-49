#!/usr/bin/env python3


def describe_game():
    import random
    num_1 = random.randint(1, 50)  # create number
    num_2 = random.randint(1, 50)  # create number
    opr = random.choice('+-*')
    res_exm = eval(str(num_1) + opr + str(num_2))
    return (num_1, num_2, opr, res_exm)


def create_question():
    import prompt
    num_1 = describe_game[0]
    num_2 = describe_game[1]
    opr = describe_game[2]
    print('What is the result of the expression?')
    print(('Question:'), (num_1), (str(opr)), (num_2))
    player_res = prompt.integer('Your answer: ')


def evaluate_answer():
    if player_res == describe_game[3]:
        return True
    else:
        return False

