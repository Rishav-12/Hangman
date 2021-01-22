import random

with open('words.txt', 'r') as file:
    words = file.read().split("\n")

secret_word = random.choice(words)
print("_ " * len(secret_word))
unsuccessful_attempts = 0
correct_letters = []
incorrect_letters = []
to_print = []

def showAttempts(correct_letters):
	for letter in secret_word:
		if letter in correct_letters:
			print(letter + ' ', end = '')
			to_print.append(letter)
		else:
			print('_ ', end = '')
			to_print.append('_')

while True:
	to_print = []

	print('HANGMAN')
	guess = input("Enter a letter: ")
	print("Word: ")

	if guess in secret_word:
		correct_letters.append(guess)
		showAttempts(correct_letters)
	else:
		if guess not in incorrect_letters:
			incorrect_letters.append(guess)
			unsuccessful_attempts += 1
		showAttempts(correct_letters)

	print("\nAlready guessed: " + " ".join(incorrect_letters))

	if unsuccessful_attempts == 6:
		print(f"You are out of guesses\nThe word was {secret_word}")
		break
	elif  '_' not in to_print:
		print("You guessed correctly. You win!!")
		break

input()
