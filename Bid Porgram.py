from art import logo_bid
import os
clear = lambda: os.system('cls')

#if you are using python shell use the below code for
#clearing the screen, otherwise keep the one above clear = lambda ...

#clear = lambda: print ("\n" * 30)

print(logo_bid)


def find_the_heighest_bidder(bidders):
  hieghest_value = 0
  for key,value in bidders.items():
    if value > hieghest_value:
      hieghest_value = value
  highest_one = [key for k,v in bidders.items() if v == hieghest_value]
  print(f"The highest value goes for {highest_one[0]}")


answer = True

name_bid = {}


while answer:
  name = input("Please enter your name\n")
  bid = int(input("Please enter your bid\n"))
  name_bid[name] = bid
  play_more = input("Is there any other users?\n")
  clear()
  if play_more == "no":
    answer = False
    find_the_heighest_bidder(name_bid)
