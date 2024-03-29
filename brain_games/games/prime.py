def create_game():
    import random
    num_1 = random.randint(1, 100)  # create number
    k = 2
    if num_1 == 1 or num_1 == 2:
        num_check = True
    else:
        while k < num_1:
            if num_1 % k == 0:
                num_check = False
                break
            else:
                num_check = True
                k = k + 1
    data_1 = num_1, num_check
    return data_1


def create_question(data_1):
    import prompt
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    print('Question: ' + str(data_1[0]))  # request + created number
    player_answer = prompt.string('Your answer: ')  # player inputs number
    data_2 = data_1[1], player_answer
    return data_2


def evaluate_answer(data_2):
    if data_2[0] is True and data_2[1] == 'yes':  # right answers even
        print('Correct!')
        return True
    elif data_2[0] is False and data_2[1] == 'no':  # right answers not even
        print('Correct!')
        return True
    elif data_2[0] is True and data_2[1] == 'no':  # incorrect answer even
        print('"no" is wrong answer ;(. Correct answer was "yes".')
        return False
    elif data_2[0] is False and data_2[1] == 'yes':  # incorrect answer not even
        print('"yes" is wrong answer ;(. Correct answer was "no".')
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
