def create_game():
    import random
    ran_num = random.randint(1, 100)
    data_1 = ran_num
    return data_1

def create_question(data_1):
    import prompt
    print('Answer "yes" if the number is even, otherwise answer "no"')
    print('Question ' + str(data_1))  # request + created number
    player_ans = prompt.string('Your answer: ')  # just string + player inputs number
    data_2 = (player_ans, data_1)
    return data_2

def evaluate_answer(data_2):
    if data_2[1] % 2 == 0 and data_2[0] == 'yes':  # count right answers even
        print('Correct!')
        return True
    elif data_2[1] % 2 == 1 and data_2[0] == 'no':  # count right answers not even
        print('Correct!')
        return True
    elif data_2[1] % 2 == 0 and data_2[0] == 'no':  # incorrect answer even
        print('"no" is wrong answer ;(. Correct answer was "yes"')
        return False
    elif data_2[1] % 2 == 1 and data_2[0] == 'yes':  # incorrect answer not even
        print('"yes" is wrong answer ;(. Correct answer was "no"')
        return False
    else:
        return False


def play():
    data_1 = create_game()
    data_2 = create_question(data_1)
    data_3 = evaluate_answer(data_2)
    return data_3


def main():
    data_1 = create_game()
    data_2 = create_question(data_1)
    evaluate_answer(data_2)

if __name__ == '__main__':
    main()
