def game():
    import prompt
    import random
    ran_num = random.randint(1, 100)  # create number
    print('Answer "yes" if the number is even, otherwise answer "no"')  # just string
    print('Question ' + str(ran_num))  # request + created number
    player_ans = prompt.string('Your answer: ')  # just string + player inputs number
    if ran_num % 2 == 0 and player_ans == 'yes':  # count right answers even
        print('Correct!')
        return True
    elif ran_num % 2 == 1 and player_ans == 'no':  # count right answers not even
        print('Correct!')
        return True
    elif ran_num % 2 == 0 and player_ans == 'no':  # incorrect answer even
        print('"no" is wrong answer ;(. Correct answer was "yes"')
        return False
    elif ran_num % 2 == 1 and player_ans == 'yes':  # incorrect answer not even
        print('"yes" is wrong answer ;(. Correct answer was "no"')
        return False
    else:
        return False





