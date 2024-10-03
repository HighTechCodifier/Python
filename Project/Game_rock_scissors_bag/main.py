"""
This file is the main program that interacts with the user and plays the 
game. It runs the game, handles user input, and calls the functions from 
rock_scissors_bag_game.py.
"""
# Import the RockScissorsBagGame class from rock_scissors_bag_game.py
from rock_scissors_bag_game import RockScissorsBagGame

# Function to start the game
def main():
    # Create a new game object from the RockScissorsBagGame class
    game = RockScissorsBagGame()
    
    # Print a message to welcome the player
    print("\n**************************************")
    print(" Welcome to Rock, Scissors, Bag game!   ")
    print("**************************************  ")
    
    # This loop keeps the game running until the player quits
    while True:

        # Ask the player to type their choice
        player_choice = input("Choose rock, scissors, or bag (or type 'quit' to exit): ").lower()

        # If the player types 'quit', exit the game
        if player_choice == 'quit':
            print("Thanks for playing! Goodbye!\n")
            break  # Exit the loop and end the game

        # Check if the player's choice is valid (rock, scissors, or bag)
        if player_choice not in game.choices:
            print("Invalid choice! Please try again.\n")
            continue  # Go back to the start of the loop if invalid choice

        # Let the computer make its choice
        computer_choice = game.computer_choice()

        # Show the player and computer choices
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        # Decide who won and display the result
        result = game.decide_winner(player_choice, computer_choice)
        print(result + "\n")

# Run the program:
if __name__ == "__main__":
    """
    This makes sure the game starts when we run the script.
    Checks if the current file is being run directly by Python.
    ¤ If true, it means the file is being run as the main program, 
      so the code inside this block will execute.
    ¤ If the file is imported as a module in another file, the code
      inside this block will not run.
    This is useful when you want some code to run only when the file
    is executed directly, not when it's imported elsewhere.
    """
    main() # manin-function
