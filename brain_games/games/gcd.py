DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_dividers(any_num):
    dividers_list = []
    divider = any_num
    while divider > 0:
        if any_num % divider == 0:
            dividers_list.append(divider)
            divider -= 1
        else:
            divider -= 1
    return dividers_list


def get_gcd(any_list_1, any_list_2):
    list_item = 0
    shared_dividers = []
    while list_item < len(any_list_2):
        for item in any_list_1:
            if item == any_list_2[list_item]:
                shared_dividers.append(item)
            else:
                continue
        list_item += 1
    return str(shared_dividers[0])  # pick up the hihgest divider


def create_game():
    import random
    random_num_1 = random.randint(1, 100)
    random_num_2 = random.randint(1, 100)
    dividers_list_1 = get_dividers(random_num_1)
    dividers_list_2 = get_dividers(random_num_2)
    correct_answer = get_gcd(dividers_list_1, dividers_list_2)
    question = ' '.join((str(random_num_1), str(random_num_2)))
    return question, correct_answer
