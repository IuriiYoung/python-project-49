#!/usr/bin/env python3

def create_game():
    import prompt
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
    number = 0  # create list of equal diveders
    div_list = []
    while number < len(num2_list):
        for item in num1_list:
            if item == num2_list[number]:
                div_list.append(item)
            else:
                continue
        number = number + 1
    num_3 = div_list[0]  # pick up the hihgest divider
    data_1 = (num_1, num_3, num_3)
    return data_1


def create_question(data_1):
    import prompt
    print('Find the greatest common divisor of given numbers')
    print('Question:', data_1[0], data_1[1])
    player_ans = prompt.integer('Your answer: ')
    data_2 = (data_1[2], player_ans)
    return data_2


def evaluate_answer(data_2):
    if data_2[1] == data_2[0]:
        print('Correct!')
        return True
    else:
        print(data_2[1], 'is wrong answer ;(. Correct answer was', data_2[0])
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
