def game():
    import prompt
    import random
    num_1 = random.randint(1, 70)  # create number
    num_2 = random.randint(1, 5)
    num_3 = random.randint(7, 13)
    num_4 = 0
    progres = [num_1]
    while num_4 < num_3:
        progres.append(num_1 + num_2)
        num_4 = num_4 + 1
        num_1 = num_1 + num_2
    num_5 = random.randint(0, (len(progres) - 1))
    num_6 = progres[num_5]
    progres.pop(num_5)
    progres.insert(num_5, '..')
    prt = ''
    k = 0
    while k < len(progres):
        prt = prt + ' ' + str(progres[k])
        k = k + 1
    print('What number is missing in the progression?')
    print(('Question:'), (prt))
    player_res = prompt.integer('Your answer: ')
    if player_res == num_6:
        print('Correct!')
        return True
    else:
        print((player_res), ('is wrong answer ;(. Correct answer was'), (num_6))
        return False
