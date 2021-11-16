from art import logo_guess
import random

HARD_LEVEL = 5
EASY_LEVEL = 10

print(logo_guess)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

def random_generator(a=0,b=101):
  return random.randint(a,b)

random_number = random_generator()

#print(f"Pssst, the correct answer is {random_number}")



def diff_level():
  game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if game_level == "easy":
    return EASY_LEVEL
  elif game_level == "hard":
    return HARD_LEVEL


def result(rand_no, level):
  for i in range(level):
    print(f"You have {level} attempts remaining to guess the number.")
    level-=1
    number = int(input("Make a guess "))
    if number == rand_no:
      return f"You are right, the answer was {rand_no} "
    elif number > rand_no:
      print("Too high")
    elif number < rand_no:
      print("Too low")
    if level != 0:
      print("Guess again.")

  return "You lost, you run out of guesses"



print(result(random_number, diff_level()))
  
