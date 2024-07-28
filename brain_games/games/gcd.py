DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def create_game_1():
    import random
    num_1 = random.randint(1, 100)  # create number
    num1_list = []  # create 1-st list of dividers
    div = num_1
    while div > 0:
        if num_1 % div == 0:
            num1_list.append(div)
            div = div - 1
        else:
            div = div - 1
    num_2 = random.randint(1, 100)  # create number
    num2_list = []  # create 2-st list of dividers
    div = num_2
    while div > 0:
        if num_2 % div == 0:
            num2_list.append(div)
            div = div - 1
        else:
            div = div - 1
    return (num1_list, num2_list, num_1, num_2)


def create_game():
    num1_list, num2_list, num_1, num_2 = create_game_1()
    number = 0  # create list of equal diveders
    div_list = []
    while number < len(num2_list):
        for item in num1_list:
            if item == num2_list[number]:
                div_list.append(item)
            else:
                continue
        number = number + 1
    correct_answer = str(div_list[0])  # pick up the hihgest divider
    question = (num_1, num_2)
    return (question, correct_answer)


def play():
    data_1 = create_game()
    return data_1


def main():
    create_game()


if __name__ == '__main__':
    main()
