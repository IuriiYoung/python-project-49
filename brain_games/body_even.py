#!/usr/bin/env

def gen_number_answer():
    import prompt
    import random
    name = prompt.string('May I have your name? ')
    print(f'Hello,{name}!')
    count = 0
    while count < 3:
        ran_num = random.randint(1, 100)  # create number
        print('Answer "yes" if the number is even, otherwise answer "no"')  # just string
        print('Question ' + str(ran_num))  # request + created number
        player_ans = prompt.string('Your answer: ')  # just string + player inputs number
        if ran_num % 2 == 0 and player_ans == 'yes':  # count right answers even
            count = count + 1
            print('Correct!')
        elif ran_num % 2 == 1 and player_ans == 'no':  # count right answers not even
            count = count + 1
            print('Correct!')
        elif ran_num % 2 == 0 and player_ans == 'no':  # incorrect answer even
            print('"no" is wrong answer ;(. Correct answer was "yes"')
            print(f"Let's try again, {name}")
            break
        elif ran_num % 2 == 1 and player_ans == 'yes':  # incorrect answer not even
            print('"yes" is wrong answer ;(. Correct answer was "no"')
            print(f"Let's try again, {name}")
            break
        else:
            print(f"Wrong input. Let's try again {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')
