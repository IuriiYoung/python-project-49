DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def create_game():
    import random
    ran_num = random.randint(1, 100)
    question = ran_num
    if ran_num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (question, correct_answer)
