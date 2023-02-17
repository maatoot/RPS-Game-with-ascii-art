import random
#  ascii art by : wynand1004/RPS_ASCII_Art.py
scissors ="""
     SCISSORS 
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""


paper ="""
    PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

rock = """
    ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
game_images = [rock, paper, scissors]
comp_opts = ("rock","paper","scissors")
comp_choice = random.choice(comp_opts)
user_choice = input("Rock , Paper , Scissors ??\n").lower().split(" ")[0]

def the_images(comp_choice,user_choice):
    if comp_choice ==  "rock":
      print (f"The super smart computer choice is: \n{game_images[0]}")
    elif comp_choice == "paper":
      print (f"The super smart computer choice is: \n{game_images[1]}")
    elif comp_choice == "scissors":
      print (f"The super smart computer choice is: \n{game_images[2]}")
    
    if user_choice ==  "rock":
      print (f"Your choice is : \n{game_images[0]}")
    elif user_choice == "paper":
      print (f"Your choice is : \n{game_images[1]}")
    elif user_choice == "scissors":
      print (f"Your choice is : \n{game_images[2]}")
def the_game(comp_choice,user_choice):
  if (user_choice == "rock" and comp_choice == "rock") or (user_choice == "paper"  and comp_choice == "paper") or (user_choice == "scissors"  and comp_choice == "scissors"):
    print(the_images(comp_choice,user_choice))
    print (" DRAW ")
  else:
    print(the_images(comp_choice,user_choice))
    if user_choice ==  "rock" and comp_choice == "paper":
      return "YOU LOST THE GAME , PLAY AGAIN ? "
    elif user_choice == "scissors" and comp_choice == "rock":
      return  "YOU LOST THE GAME , PLAY AGAIN ? "
    elif user_choice == "paper" and comp_choice == "scissors":
     return  "YOU LOST THE GAME , PLAY AGAIN ? "
    else:
      return  "YOU WON THE GAME , PLAY AGAIN ? "



if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
  print(the_game(comp_choice,user_choice))
else:
  print("You have entered an incorrect value !! , please make sure that your spelling is correct .")
  user_choice = input("Rock , Paper , Scissors ??\n").lower()
  try:
    print(the_game(comp_choice,user_choice))
  except:
    print("Unknown error happend please restart the game")
