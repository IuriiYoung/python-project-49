#!/usr/bin/env python3

def game():
    import prompt
    import random
    import operator
    num_1 = random.randint(1, 50)  # create number
    num_2 = random.randint(1, 50)  # create number
    opr = random.choice('+-*')
    res_exm = eval(str(num_1) + opr + str(num_2))
    print('What is the result of the expression?')
    print(('Question:'), (num_1), (str(opr)), (num_2))
    player_res = prompt.integer('Your answer: ')
    if player_res == res_exm:
        print('Correct!')
        return True
    else:
        print(str(player_res), ('is wrong answer ;(. Correct answer was'), str(res_exm))
        return False







