import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(placeholder)

display = ""
number = 0
lives = 6
appear = False

while display != chosen_word and lives != 0:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed the letter '{guess}'.")

    elif number == 0:
        for letter in chosen_word:
            if letter == guess:
                display += letter
                appear = True
            else:
                display += "_"
        if not appear:
            lives -= 1
            print(f"The letter '{guess}' does not appear in the word.")
        print(stages[lives])
        print(f"****************************<???>/{lives} LIVES LEFT****************************")
        appear = False
        number += 1

    else:
        display = list(display)
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                display[index] = guess
                appear = True
        if not appear:
            lives -= 1
        print(stages[lives])
        print(f"****************************<???>/{lives} LIVES LEFT****************************")
        appear = False
        display = ''.join(display)
    print(display)

if lives == 0:
    print(f"IT WAS <{chosen_word}>! YOU LOSE")
else:
    print("YOU WIN")
