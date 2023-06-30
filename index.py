import random

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock, paper, or scissors), or 'q' to quit: ").lower()
        if choice in ['rock', 'paper', 'scissors', 'q']:
            return choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'draw'
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return 'user'
    else:
        return 'computer'

def play_round():
    user_choice = get_user_choice()
    if user_choice == 'q':
        return False

    computer_choice = get_computer_choice()

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    winner = determine_winner(user_choice, computer_choice)

    if winner == 'draw':
        print("It's a draw!")
    else:
        print(winner.capitalize(), "wins!")

    return True

def play_game():
    user_wins = 0
    computer_wins = 0
    draws = 0

    while True:
        print("\n--- New Round ---")
        print("Score: User -", user_wins, "Computer -", computer_wins, "Draws -", draws)
        if not play_round():
            break

        winner = determine_winner(user_choice, computer_choice)
        if winner == 'user':
            user_wins += 1
        elif winner == 'computer':
            computer_wins += 1
        else:
            draws += 1

    print("\nFinal Score: User -", user_wins, "Computer -", computer_wins, "Draws -", draws)
    print("Thanks for playing!")

play_game()
