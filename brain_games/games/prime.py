DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime_check(num):
    k = 2
    correct_answer = 'yes'
    while k < num:
        if num % k == 0:
            correct_answer = 'no'
            break
        else:
            k = k + 1
    return correct_answer


def create_game():
    import random
    num_1 = random.randint(1, 100)  # create number
    correct_answer = prime_check(num_1)
    return (num_1, correct_answer)
