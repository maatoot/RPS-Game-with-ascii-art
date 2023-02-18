import random

# Define the game images as a dictionary
game_images = {
    "rock": """
        ROCK
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    "paper": """
        PAPER
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    """,
    "scissors": """
        SCISSORS
        ---'   ____)____
              ______)
           __________)
          (____)
        ---.__(___)
    """
}

def get_user_choice():
    
    #Get the user choice and vaildate it 
    user_choice = ""
    while user_choice not in game_images.keys():
        user_choice = input("Rock, paper, or scissors? ").lower().strip()
        if user_choice not in game_images.keys():
            print("Invalid choice. Please choose rock, paper, or scissors.")
    return user_choice

def play_game(comp_choice, user_choice):
    # Determine the winner of the game 

    if comp_choice == user_choice:
        print("It's a tie!")
    elif (comp_choice == "rock" and user_choice == "scissors") or (comp_choice == "paper" and user_choice == "rock") or (comp_choice == "scissors" and user_choice == "paper"):
        print("You lose!")
    else:
        print("You win!")

    # print the computer's and user's choices
    print("Computer's choice:")
    print(game_images[comp_choice])
    print("Your choice:")
    print(game_images[user_choice])

# Main game loop
while True:
    # get the computer's choice randomly 
    comp_choice = random.choice(list(game_images.keys()))

    # Get the user's choice by the get_user_choice() function in line 33
    user_choice = get_user_choice()

    play_game(comp_choice, user_choice)

    # if the user says anything that isn't y the loop breaks and the program will be ended .
    play_again = input("Do you want to play again?? (y/n) ").lower().strip()
    if play_again != "y":
        break
