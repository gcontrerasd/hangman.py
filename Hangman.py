import random

def choose_word():
	words = ["apple"]
	return random.choice(words)

def display_word(word, guessed_letters):
		display = ""
		for letter in word:
			if letter in guessed_letters:
				display += letter
			else:
				display += "-"
		return display

def hangman():
		word = choose_word()
		guessed_letters = []
		attempts = 6

		print("The Hangman!")
		print(display_word(word, guessed_letters))

		while attempts > 0:
			guess = input ("Could you guess a letter: ").lower()

			if len(guess) != 1 or not guess.isalpha():
				print("Just put one letter, don't cheat")
				continue

			guessed_letters.append(guess)
			
			if guess not in word:
				attempts -= 1
				print(f"Wrong guess! {attempts} attempts left.")
				if attempts == 0:
					print ("Sorry, you have no more attemps. The word was:", word)
					break

			else:
				print ("Correct guess!")

			current_display = display_word(word, guessed_letters)
			print(current_display)

			if "-" not in current_display:
				print ("Great job! You guessed the word!")
				break
				
if __name__ == "__main__":
    hangman()