DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


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
    if num_check is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (num_1, correct_answer)


def play():
    data_1 = create_game()
    return data_1


def main():
    create_game()


if __name__ == '__main__':
    main()
