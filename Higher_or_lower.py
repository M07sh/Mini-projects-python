from art import logo_higher,vs
from game_data import data
import random
import os
clear = lambda: os.system('cls')

#if you are using python shell use the below code for
#clearing the screen, otherwise keep the one above clear = lambda ...

#clear = lambda: print ("\n" * 30)

DATA_A = []
DATA_B = []
USED_DATA = []

def choose_date(data_set):
  """ The function returns the data needed for the game"""
  DATA_A.append(random.choice(data))
  while len(data) != len(DATA_A):
    single_data = random.choice(data)
    if single_data not in DATA_B and single_data not in DATA_A:
      DATA_B.append(single_data)
      DATA_A.append(single_data)

def reformat_data(data):
  data_name = data["name"]
  data_discr = data["description"]
  data_country = data["country"]
  return f'{data_name}, a {data_discr}, from {data_country}.'

def game():
  print(logo_higher)
  choose_date(data)
  count=0
  game_over = False
  while not game_over:
    print(f"Compare A: {reformat_data(DATA_A[count])}")

    print(vs)

    print(f"Compare B: {reformat_data(DATA_B[count])}")

    A,B = DATA_A[count]['follower_count'],DATA_B[count]['follower_count']
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    clear()
    print(logo_higher)

    if A<B and answer == "A" or B<A and answer =="B":
      game_over = True
    else:
      count+=1 
      print(f"You're right! Current score: {count}.")

  print(f"Sorry, that's wrong. Final score: {count}")

game()
    


