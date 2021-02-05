import time, random

def start_game():
	player_name = input("What is your name? : ")
	print("Ok", player_name, "Let's begin our game!")
	token = 0
	time.sleep(1)
	while token != 1:
		want = str(input("\nWant to start a game?\nPress 'y' for yes\nor\nPress 'n' for no.\n"))
		if want == 'y':
			time.sleep(1)
			break
		elif want == 'n':
			time.sleep(1)
			break
		else:
			time.sleep(1)
			continue
	if want == 'y':
		print("\nLet's GO!!!\n")
		time.sleep(1)
		return #อิหยังวะ
	elif want == 'n':
		print("So sad TwT. Good bye.\n")
		time.sleep(1)
		exit()

def input_guess():
	global guess_already
	token = 0
	while token != 1:
		user_guess = input("Guess an alphabet : ")
		if user_guess.isalpha() == True:
			token_pass = 0
			for i in guess_already:
				if user_guess == i:
					time.sleep(1)
					print("This word is already used.")
				else:
					token_pass = token_pass + 1
					if token_pass == len(guess_already):
						token = token + 1
		else:
			time.sleep(1)
			print("Not an alphabet...")
	return user_guess

def game():
	global word
	global guess_already
	global guess_right
	global guess_wrong
	token_win = 0
	remain = len(word)
	display()
	while remain != 0:
		j = input_guess()
		token_wrong = 0
		for i in word:
			if j == i:
				guess_already.append(j)
				guess_right.append(j)
				token_win = token_win + 1
				if i == word[len(word)-1]:
					time.sleep(1)
					print("correct")
					break 
			else:	
				token_wrong = token_wrong + 1		
				if i == word[len(word)-1] and token_wrong == len(word):
					guess_already.append(j)
					guess_wrong.append(j)
					remain = remain - 1
					time.sleep(1)
					print("Your guess is wrong. Please guess again.")
		time.sleep(1)
		hangman_display(remain)
		display()
		time.sleep(1)
		print("Your remain : ", remain)
		time.sleep(0.5)
		print("Your wrong word : ", guess_wrong)
		time.sleep(0.5)
		print("\n")
		if token_win == len(word):
			break
	if token_win == len(word):
		time.sleep(1)
		print("==Hell Yeah. You are winner.==")
		exit()
	else:
		time.sleep(1)
		print("The correct word is", word, "!!!")
		print("==!!!Such a loser!!!==")
		exit()

def display():
	my_string = word #i
	print("\n==========")
	for i in my_string:
		token = 0
		for j in guess_right:
			if j == i:
				print(i, end="")
				break
			else:
				token = token + 1
				if token == len(guess_right):
					print("?", end="")
	print("\n==========")
	if word == "tenet":
		print("Hint : Name of movie\n")
	elif word == "steak":
		print("Hint : Food\n")
	elif word == "kangaroo":
		print("Hint : animal\n")
	elif word == "nucleus":
		print("Hint : Biology\n")
	elif word == "television":
		print("Hint : Electrical equipment\n")
	else:
		print("Error...")
		
def hangman_display(guesses):
		if guesses == 0:
			print ("________      ")
			print ("|      |      ")
			print ("|             ")
			print ("|             ")
			print ("|             ")
			print ("|             ")
		elif guesses == 1:
			print ("________      ")
			print ("|      |      ")
			print ("|      0      ")
			print ("|             ")
			print ("|             ")
			print ("|             ")
		elif guesses == 2:
			print ("________      ")
			print ("|      |      ")
			print ("|      0      ")
			print ("|     /       ")
			print ("|             ")
			print ("|             ")
		elif guesses == 3:
			print ("________      ")
			print ("|      |      ")
			print ("|      0      ")
			print ("|     /|      ")
			print ("|             ")
			print ("|             ")
		elif guesses == 4:
			print ("________      ")
			print ("|      |      ")
			print ("|      0      ")
			print ("|     /|\     ")
			print ("|             ")
			print ("|             ")
		elif guesses == 5:
			print ("________      ")
			print ("|      |      ")
			print ("|      0      ")
			print ("|     /|\     ")
			print ("|     /       ")
			print ("|             ")
		else:
			print ("________      ")
			print ("|      |      ")
			print ("|      0      ")
			print ("|     /|\     ")
			print ("|     / \     ")
			print ("|             ")


list_word = ["tenet", "steak", "kangaroo", "nucleus", "television"]
word = random.choice(list_word)
guess_right = ['1']
guess_wrong = []
guess_already = ['1']
start_game()
game()



