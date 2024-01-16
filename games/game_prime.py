def game():
    import prompt
    import random
    num_1 = random.randint(1, 100)  # create number
    print(num_1)
    k = 2
    num_ans = True
    while k < num_1:
        if num_1 == 1 or num_1 == 2:
            num_ans = True
            break
        elif num_1 % k == 0:
            num_ans = False
            break
        else:
            num_ans = True
            k = k + 1
    print('Answer "yes" if given number is prime, otherwise answer "no"')  # just string
    print(('Question '), (num_1))  # request + created number
    player_ans = prompt.string('Your answer: ')  # just string + player inputs number
    if num_ans == True and player_ans == 'yes':  # count right answers even
        print('Correct!')
        return True
    elif num_ans == False and player_ans == 'no':  # count right answers not even
        print('Correct!')
        return True
    elif num_ans == True and player_ans == 'no':  # incorrect answer even
        print('"no" is wrong answer ;(. Correct answer was "yes"')
        return False
    elif num_ans == False and player_ans == 'yes':  # incorrect answer not even
        print('"yes" is wrong answer ;(. Correct answer was "no"')
        return False
    else:
        return False

