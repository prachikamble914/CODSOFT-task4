print("*******Rock-Paper-Scissors Game*******")
import random

options = ("rock","paper","sicssors")
running = True

while running:
    user_choice = None
    computer_choice = random.choice(options)

    while user_choice not in options:
        user_choice = input("enter a choice(rock,paper,secissors):")
        print(f"user_choice: {user_choice}")
        print(f"computer_choice:{computer_choice}")

        if  user_choice ==  computer_choice :
            print("it is a tie!")
        elif  user_choice == "rock" and  computer_choice  == "scissors":
            print("you win!")
        elif  user_choice == "paper" and  computer_choice  == "rocks":
            print("you win!")
        elif  user_choice == "scissors" and  computer_choice  == "paper":
            print("you win!")
        else:
            print("you lose!")

            if not input(" want to play another round? (y/n):").lower() == "y":
                running = False

                print("Thanks for playing!")



