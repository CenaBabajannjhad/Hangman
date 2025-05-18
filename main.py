from hangman_art import stages
from init import init_game
from randomly_word import randomly_chosen_word as chosen_word_func
from message_printer import line_printer

is_game_finished = False
lives = 6
display = []

# greeting
init_game()
# randomly choose a word
chosen_word = chosen_word_func()
# display for each letter in chosen_word
word_len = len(chosen_word)
for _ in range(word_len) :
    display.append("_")
print(display)
line_printer()
# game logic
while not is_game_finished :
    # ask the user to guess the letter
    guess = input("Guess Letter : ")
    # if the user enters a duplicate character
    if guess in display :
        print(f"You've already guessed : {guess}")
    # check if the letter is one of the letters in the chosen_word
    for position in range(word_len) :
        letter = chosen_word[position]
        if letter == guess :
            display[position] = letter
    # if the user enters a wrong character that is not in the word
    if guess not in chosen_word :
        lives -= 1
        print(f"your guess {guess}, that's not in the word. you lose a life")
        line_printer()
        print(stages[lives])
        line_printer()
        # if lives finished
        if lives == 0 :
            is_game_finished = True
            line_printer()
            print("game over")
            line_printer()
            print(f"the word was : ***{chosen_word}***")
            line_printer()

    print(display)
    # if game finished
    if "_" not in display :
        is_game_finished = True
        line_printer()
        print("You Win")
        line_printer()






