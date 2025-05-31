import random
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])
def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (
        (player == 'rock' and computer == 'scissors') or
        (player == 'scissors' and computer == 'paper') or
        (player == 'paper' and computer == 'rock')
    ):
        return "You win!"
    else:
        return "Computer wins!"
def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        player_choice = input("Choose rock, paper, or scissors (or type 'quit' to exit): ").lower()
        if player_choice == 'quit':
            print("Thanks for playing!")
            break
        elif player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = get_winner(player_choice, computer_choice)
        print(result)
        print()
play_game()
