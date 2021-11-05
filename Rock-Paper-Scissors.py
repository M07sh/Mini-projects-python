import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

RPS = [rock,paper,scissors]
random_choice = random.randint(0,2)
computer_choice = RPS[random_choice]
game_over = False

while not game_over:

    player_choice = int(input("What do you choose, type 0 for rock 1 for paper and 2 for scissors\n "))

    if player_choice >= 0 and player_choice < 3:
      print(f"The computer choice is {computer_choice},\nYour choice is {RPS[player_choice]} ")
    else:
      print("You choose an invalid number, you lose!")


    if random_choice == player_choice :
      print("It's draw !")
    elif (random_choice == 0 and player_choice == 2) or (random_choice >  player_choice):
      print("You lose !")
    elif ((player_choice == 0 and random_choice == 2) or (player_choice > random_choice )) and (player_choice >= 0 and player_choice < 3):
      print("You win !")

    play_again = input("Do you want to play again? type y for yest, or n for no: ")

    if play_again == "n":
        game_over = True
        
