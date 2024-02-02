def create_game():
    import random
    num_1 = random.randint(1, 70)  # create number
    num_2 = random.randint(1, 5)  # create coefficient
    num_3 = random.randint(7, 13)   # create the quantity of progression
    num_4 = 0
    progres = [num_1]  # create 1-st number of progression
    while num_4 < num_3:
        progres.append(num_1 + num_2)
        num_4 = num_4 + 1
        num_1 = num_1 + num_2
    num_5 = random.randint(0, (len(progres) - 1))  # define number for excluding
    num_6 = progres[num_5]  # define the value of the excluded number
    progres.pop(num_5)  # exclude the number
    progres.insert(num_5, '..')  # insert the dots
    string_for_question = ''
    k = 0
    while k < len(progres):
        string_for_question = string_for_question + ' ' + str(progres[k])
        k = k + 1
    data_1 = string_for_question, num_6
    return data_1


def create_question(data_1):
    import prompt
    print('What number is missing in the progression?')
    print('Question:', data_1[0])
    player_answer = prompt.integer('Your answer: ')
    data_2 = player_answer, data_1[1]
    return data_2


def evaluate_answer(data_2):
    if data_2[0] == data_2[1]:
        print('Correct!')
        return True
    else:
        print(data_2[0], 'is wrong answer ;(. Correct answer was', data_2[1])
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
