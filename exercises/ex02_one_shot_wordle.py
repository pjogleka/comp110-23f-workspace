"""Wordle game with one shot at winning!"""

__author__ = "730569615"

# Define variables, then intake and check user input
secret_word = "python"
length = len(secret_word)
input_word = input(f"What is your {length}-letter guess? ")
while len(input_word) != length:
    input_word = input(f"That was not {length} letters! Try again: ")

# Define variables then test user input
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index = 0
boxes = ""
while index < length:
    if input_word[index] == secret_word[index]:
        boxes += GREEN_BOX
    else:
        letter_exists = False
        for i in range(len(secret_word)):
            if input_word[index] == secret_word[i]:
                letter_exists = True
        if letter_exists:
            boxes += YELLOW_BOX
        else:
            boxes += WHITE_BOX
    index += 1
print(boxes)
if input_word != secret_word:
    print("Not quite! Play again soon!")
elif input_word == secret_word:
    print("Woo! You got it!")
