import time
from random import *

# Variables

wordList = ["alpinista", "computadora", "senderismo", "autopista", "atmosfera", "estuchera", "eclipse", "cataclismo",
            "chapuzon", "conmutador", "helipuerto"]
attempts = 6
goodChoices = 0
mistakenWords = []
rightWords = []
endedGame = False


# Functions

def choose_word(wlist):
    wordchoice = choice(wlist)
    unique_words = len(set(wordchoice))
    return wordchoice, unique_words


def ask_letter():
    selected_word = ''  # Letra elegida
    is_valid = False
    abecedary = 'abcdefghijklmnñopqrstuvwxyz'

    while not is_valid:
        selected_word = input(f" Please select a letter: ").lower()
        if selected_word in abecedary and len(selected_word) == 1:
            is_valid = True
        else:
            print("The selected item is invalid. Please select a letter")

    return selected_word


def show_new_len(selected_letter):  # Palabra elegida
    hidden_list = []

    for lt in selected_letter:
        if lt in rightWords:
            hidden_list.append(lt)
        else:
            hidden_list.append('-')

    print(' '.join(hidden_list))


def validate_letter(selected_letter, hiden_word, lifes, coincidences):
    end = False

    if selected_letter in hiden_word and selected_letter not in rightWords:
        rightWords.append(selected_letter)
        coincidences += 1
    elif selected_letter in hiden_word and selected_letter in rightWords:
        print("You already selected that letter. Try with another one")
    else:
        mistakenWords.append(selected_letter)
        lifes -= 1

    if lifes == 0:
        end = perder()
    elif coincidences == unique_words:
        end = win(hiden_word)

    return lifes, end, coincidences


def perder():
    print("You have run out of lives. The word was: " + palabra)
    return True


def win(discovered_word):

    print("You won. Congratulations!! The word was: " + palabra)
    return True


#  Event Listeners

palabra, unique_words = choose_word(wordList)

while not endedGame:
    show_new_len(palabra)
    print("Mistaken words: " + '-'.join(mistakenWords))
    print(f"Attempts: {attempts} ")
    letra = ask_letter()

    attempts, ended, goodChoices = validate_letter(letra, palabra, attempts, goodChoices)

    endedGame = ended

