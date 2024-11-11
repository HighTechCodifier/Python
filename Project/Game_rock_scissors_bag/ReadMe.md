
Rock-Scissors-Bag Game
=======================

This is a simple text-based Python game where you play "Rock, Scissors, Bag" (similar to Rock-Paper-Scissors) against the computer. The game is designed to be easy to understand and suitable for programming beginners.

Game Rules:
    ¤ You choose either rock, scissors, or bag.
    ¤ The computer randomly chooses one of the three as well.
    ¤ The game compares your choice to the computer's choice and determines the winner based on these rules:

        ¤ Rock beats scissors.
        ¤ Scissors beats bag.
        ¤ Bag beats rock.
        ¤ If both choose the same, it's a tie.
    ¤ You can keep playing as many rounds as you like until you decide to quit.

Files in the Project:
    1. rock_scissors_bag_game.py: This file contains the game logic, such as the rules and how the computer chooses its move.
    2. main.py: This is the main program file. It runs the game, handles user input, and calls the functions from rock_scissors_bag_game.py.
    3. README.md: This file provides instructions and information about the project.

How to Run the Game
    Prerequisites:
    You need to have Python installed on your computer. If you don't have it, download it from python.org.

    Steps
        1. Download the files: Make sure both rock_scissors_bag_game.py and main.py are in the same folder.
        2. Run the Game:
            ¤ Open a terminal or command prompt.
            ¤ Navigate to the folder where the files are located.
            ¤ Run the following command:
            python main.py
        3. Play the Game:
            ¤ You will be prompted to enter your choice: rock, scissors, or bag.
            ¤ The game will compare your choice with the computer's and display the result.
            ¤ Type quit to exit the game.

Example Game Play:

**************************************
 Welcome to Rock, Scissors, Bag game!
**************************************
Choose rock, scissors, or bag (or type 'quit' to exit): rock

You chose: rock
Computer chose: scissors
You win!

Choose rock, scissors, or bag (or type 'quit' to exit): bag

You chose: bag
Computer chose: rock
You win!

Choose rock, scissors, or bag (or type 'quit' to exit): quit
Thanks for playing! Goodbye!
