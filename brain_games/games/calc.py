DESCRIPTION = 'What is the result of the expression?'


def create_game():
    import random
    num_1 = random.randint(1, 50)  # create number
    num_2 = random.randint(1, 50)  # create number
    opr = random.choice('+-*')
    correct_answer = str(eval(str(num_1) + opr + str(num_2)))
    question = ' '.join((str(num_1), str(opr), str(num_2)))
    return (question, correct_answer)


def play():
    data_1 = create_game()
    return data_1


def main():
    create_game()


if __name__ == '__main__':
    main()
