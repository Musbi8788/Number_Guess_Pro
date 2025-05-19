import random
from art import num

# display the art design for the number guessing game
print(num)

# start with 0 answer
answer = 0
user_guess = 0

# user have only 10 attempt to guess
to_try = 10
# the attempt user take before getting it right answer
to_get_it = 0


# random answer from randint , set the level.
# level 1 guess from 1-50
level1 = random.randint(1,50)
# level 2 guess from 1-100
level2 = random.randint(1,100)
# level 2 guess from 1-150
level3 = random.randint(1,150)


# user which level did they want to play.
user_input = int(input("Which level did you want to play (1 / 2/ 3/)>> "))

# game is active
game_is_going = True
while game_is_going:
	# handle error
	try:
		# Set the answers base on the user chosen level
		user_level = user_input
		if user_level == 1:
			answer = level1
			# print(answer)
		elif user_level == 2:
			answer = level2
			# print(answer)
		elif user_level == 3:
			answer = level3
			# print(answer)

		else:
			print("Invalid Error Try Again.")
			game_is_going = False
			break

	except ValueError as error:
		print("\nSorry, only numbers are allowed.")

	else:
		to_try -= 1
		to_get_it += 1
		try:
			# user guess number
			user_guess = int(input("Guess a number? "))

		except ValueError as error:
			print("\nSorry, only numbers are allowed.")

		finally:
			# user guess is too high give them another chance
			if user_guess > answer:
				print('Too high. Try Again!!')
				print(f'You have {to_try} Remaining.\n')

			# user's guess is too low give them another chance
			elif user_guess < answer:
				print('Too low. Try Again')
				print(f'You have {to_try} Remaining.\n')

			# user got the right answer
			elif user_guess == answer:
				print('Waw you got it..')
				print(f'You have try {to_get_it} attempts  before getting in the right number.')
				# stop the loop
				game_is_going = False

			# stop the game when the user attempt is less than 1
			if to_try < 1:
				print(f'You lose the answer was {answer}.')
				print("thanks for playing my game")
				game_is_going = False
