from random import choice
from hangman_words import word_list

def randomly_chosen_word() :
    return choice(word_list)
    