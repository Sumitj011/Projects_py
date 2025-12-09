# Project -(Rock–Paper–Scissors)-------------------------------------------------------

import random

player_1 = input("Lets play rock paper scissor , choose one!: ")
option = ("rock", "paper", "scissor")
player_2 = random.choice(option)

if player_1 == player_2:
    print("its a draw ")
elif player_1 == "rock" and player_2 == "scissor":
    print("player_1 wins")
elif player_1 == "paper" and player_2 == "rock":
    print("player_1 wins")
elif player_1 == "scissor" and player_2 == "paper":
    print("player_1 wins")
else:
    print("player_2 wins ")

# It can also be written as

player_1 = input("Let's play rock paper scissor, choose one!: ")
option = ("rock", "paper", "scissor")
player_2 = random.choice(option)

print(f"Computer chose: {player_2}")

if player_1 == player_2:
    print("It's a draw")
elif (player_1 == "rock" and player_2 == "scissor") or \
     (player_1 == "paper" and player_2 == "rock") or \
     (player_1 == "scissor" and player_2 == "paper"):
    print("Player 1 wins")
else:
    print("Computer wins")
