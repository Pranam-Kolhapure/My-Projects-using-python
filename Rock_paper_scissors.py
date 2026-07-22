import random

choices = ["rock", "paper", "scissors"]

print("=== Rock Paper Scissors ===")

while True:
    user = input("Enter rock, paper, or scissors: ").lower()

    if user not in choices:
        print("Invalid choice! Try again.\n")
        continue

    computer = random.choice(choices)

    print(f"\nYour choice: {user}")
    print(f"Computer choice: {computer}")

    # Check winner
    if user == computer:
        print("It's a tie!")

    elif (
            (user == "rock" and computer == "scissors") or
            (user == "paper" and computer == "rock") or
            (user == "scissors" and computer == "paper")
    ):
        print("You win!")

    else:
        print("Computer wins!")

    play_again = input("\nPlay again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break

    print()


