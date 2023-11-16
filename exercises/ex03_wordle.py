"""Improved Wordle with functions."""


__author__ = '730569615'


def contains_char(word: str, letter: str) -> bool:
    """Searches word for letter."""
    assert len(letter) == 1
    index = 0
    letter_exists = False
    while index < len(word):
        if word[index] == letter:
            letter_exists = True
        index += 1
    return letter_exists
        

def emojified(guess: str, secret: str) -> str:
    """Codifies guess."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index = 0
    codified = ""
    while index < len(guess):
        if guess[index] == secret[index]:
            codified += GREEN_BOX
        elif contains_char(secret, guess[index]):
            codified += YELLOW_BOX
        else:
            codified += WHITE_BOX
        index += 1
    return codified


def input_guess(exp_length: int) -> str:
    """Prompts user until guess is correct length."""
    guess = input(f"Enter a {exp_length} character word: ")
    while len(guess) != exp_length:
        guess = input(f"That wasn't {exp_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret = "codes"
    turns = 0
    won = False
    while turns < 6 and won == False:
        print(f"=== Turn {turns + 1}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            won = True
        turns += 1
    if won:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()