"""EX01 - Chardle - A cute step toward Wordle."""


__author__ = "730569615"


word = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
letter = input("Enter a single character: ")
if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + str(letter) + " in " + str(word))
n = 0
for i in range(len(word)):
    if word[i] == str(letter):
        print(str(letter) + " found at index " + str(i))
        n += 1
if n == 0:
    print("No instances of " + str(letter) + " found in " + str(word))
elif n == 1:
    print("1 instance of " + str(letter) + " found in " + str(word))
else:
    print(str(n) + " instances of " + str(letter) + " found in " + str(word))
