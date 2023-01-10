import random

white_possibles = list(range(1, 70))
red_possibles = list(range(1, 27))

tickets_per_drawing = 1
num_drawings = 1

total_spent = 0
earnings = 0

times_won = {
    '5+P': 0,
    '5': 0,
    '4+P': 0,
    '4': 0,
    '3+P': 0,
    '3': 0,
    '2+P': 0,
    '1+P': 0,
    'P': 0,
    '0': 0
}

def calc_win_amt (my_numbers, winning_numbers):
    win_amt = 0

    white_match = len(my_numbers["whites"].intersection(winning_numbers["whites"]))
    power_match = (my_numbers['red'] == winning_numbers['red'])

    return win_amt

for drawing in range(num_drawings):
    white_drawing = set(random.sample(white_possibles, k=5))
    red_drawing = random.choice(red_possibles)

    winning_numbers = {'whites': white_drawing, 'red': red_drawing}

    for ticket in range(tickets_per_drawing):
        total_spent += 2
        my_whites = set(random.sample(white_possibles, k=5))
        my_red = random.choice(red_possibles)

    my_numbers = {'whites': my_whites, 'red': my_red}

    #calc_win_amt