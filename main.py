import random

random_number = random.randint(1,101)
guess_remaining = ''
end_game = False
print("\nWelcome to the number guessing game.\n")
print("I am thinking of a number between 1 and 100.\n")
diff_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if diff_level == "easy":
  guess_remaining = 10  
elif diff_level == "hard":
  guess_remaining = 5


def guess_number():
  global guess_remaining
  print(f"You have {guess_remaining} attempts to guess the number.")
  guess = int(input("Make a guess: "))
  if guess > random_number:
    print("Too High\n")
    print("Guess Again\n")
    return guess_remaining - 1
      
  elif guess < random_number:
    print("Too Low.")
    print("Guess Again\n")
    return guess_remaining - 1

  elif guess == random_number:
    print("Congratulations. You guessed it right.")
    print("Guess Again\n")
    return 

while not end_game:
  if guess_remaining == 0:
    print("You have attempted maximum times and game is over now. You Lost.")
    end_game = True
  else:
    guess_remaining = guess_number()
