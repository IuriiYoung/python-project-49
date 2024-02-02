#!/usr/bin/env python3

def create_game():
    import random
    num_1 = random.randint(1, 50)  # create number
    num_2 = random.randint(1, 50)  # create number
    opr = random.choice('+-*')
    res_exm = eval(str(num_1) + opr + str(num_2))
    data1 = (num_1, num_2, opr, res_exm)
    return data1


def create_question(data1):
    import prompt
    print('What is the result of the expression?')
    print(('Question:'), (data1[0]), (data1[2]), (data1[1]))
    player_ans = prompt.integer('Your answer: ')
    res_top = data1[3]
    data2 = (player_ans, res_top)
    return data2


def evaluate_answer(data2):
    if data2[0] == data2[1]:
        print ('Correct!')
        return True
    else:
        print (data2[0], 'is wrong answer ;(. Correct answer was', data2[1])
        return False

def play():
    data1 = create_game()
    data2 = create_question(data1)
    data3 = evaluate_answer(data2)
    return data3

def main():
    data1 = create_game()
    data2 = create_question(data1)
    evaluate_answer(data2)


if __name__ == '__main__':
    main()
