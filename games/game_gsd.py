#!/usr/bin/env python3

def game():
    import prompt
    import random
    num_1 = random.randint(1, 100)  # create number
    num1_list = []
    div = num_1
    while div > 0:
        if num_1 % div == 0:
            num1_list.append(div)
            div = div - 1
        else:
            div = div - 1
    num_2 = random.randint(1, 100)  # create number
    num2_list = []
    div = num_2
    while div > 0:
        if num_2 % div == 0:
            num2_list.append(div)
            div = div - 1
        else:
            div = div - 1
    number = 0
    div_list = []
    while number < len(num2_list):
        for item in num1_list:
            if item == num2_list[number]:
                div_list.append(item)
            else:
                continue
        number = number + 1
    high_div = div_list[0]
    print('Find the greatest common divisor of given numbers')
    print(('Question:'), (num_1), (num_2))
    player_res = prompt.integer('Your answer: ')
    if player_res == high_div:
        print('Correct!')
        return True
    else:
        print((player_res), ('is wrong answer ;(. Correct answer was'), (high_div))
        return False
