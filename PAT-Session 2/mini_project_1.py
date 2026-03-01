import random
choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0
print("If you neeed to quit from the game just type "'quit'"")
while True:

    player_choice = input("Enter your choice (rock, paper, or scissors): ")

    if player_choice == 'quit':
        print("-" * 30)
        print("Game Over - Final Score")
        print(f"You: {player_score} | Computer: {computer_score}")

        if player_score > computer_score:
            print("You win the overall game!")
        elif computer_score > player_score:
            print("Computer wins the overall game!")
        else:
            print(" It's a draw!")
        print("-" * 30)
        break


    if player_choice not in choices:
        print("Invalid choice. Please type 'rock', 'paper', or 'scissors'.")
        continue


    computer_choice = random.choice(choices)
    print(f"Computer chose: **{computer_choice}**")

    if player_choice == computer_choice:
        print("It's a tie!")


    elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "paper" and computer_choice == "rock") or \
            (player_choice == "scissors" and computer_choice == "paper"):
        print("You win this round!")
        player_score += 1

    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Current Score: You {player_score} - {computer_score} Computer\n")

