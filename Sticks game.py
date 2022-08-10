from random import *

# Stick list
stick_list = ['-', '--', '---', '----']

# Shuffle the sitcks

def shuffle_sticks(sticks):
    shuffle(sticks)
    return sticks


# User Choice

def user_choice():
    attempt = ''
    while attempt not in ['1', '2', '3', '4']:
        attempt = input(f" Please select a number between 1 and 4: ")
    return int(attempt)

# Choice revision

def attempt_revision(stick_list, attempt):
    if stick_list[attempt - 1] == '-':
        print(f"Your stick was the smallest. You lost ")
    else:
        print(f"You are save")

    print(f"Your number represent the {stick_list[attempt - 1]}")

shuffled_sticks = shuffle_sticks(stick_list)
selection = user_choice()
attempt_revision(shuffled_sticks, selection)