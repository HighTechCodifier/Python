"""
This file contains the class RockScissorsBagGame, which holds the game logic.
This class contains the game logic, such as the rules and how the computer 
chooses its move.
"""

import random  # We use this to let the computer make a random choice

# This class handles the game logic for Rock, Scissors, Bag
class RockScissorsBagGame:
    def __init__(self):
        # The 3 choices in the game: rock, scissors, or bag
        self.choices = ["rock", "scissors", "bag"]

    # This method randomly picks one choice for the computer
    def computer_choice(self):
        return random.choice(self.choices)

    # This method decides who wins: player or computer
    def decide_winner(self, player, computer):
        if player == computer:
            return "It's a tie!"  # If both choose the same, it's a tie
        
        # Check all possible ways the player can win
        if (player == "rock" and computer == "scissors") or \
           (player == "scissors" and computer == "bag") or \
           (player == "bag" and computer == "rock"):
            return "You win!"
        
        # If the player didn't win or tie, the computer wins
        return "Computer wins!"
