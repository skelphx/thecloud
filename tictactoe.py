#!/usr/bin/env python3
"""
Tic-Tac-Toe Game
A complete implementation of the classic Tic-Tac-Toe game in Python.
Author: Python Course
Date: 2025
"""

import os
import sys

class TicTacToe:
    def __init__(self):
        """Initialize the game with an empty board and set first player."""
        self.board = [' ' for _ in range(9)]  # 9 empty spaces
        self.current_player = 'X'
        self.game_over = False
        self.winner = None

    def display_board(self):
        """Display the current state of the game board."""
        # Clear screen for better user experience
        os.system('cls' if os.name == 'nt' else 'clear')

        print("\n" + "="*30)
        print("     TIC-TAC-TOE GAME")
        print("="*30)
        print("\nCurrent Player:", self.current_player)
        print("\nBoard positions (1-9):")
        print(" 1 | 2 | 3 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 7 | 8 | 9 ")
        print("\nGame Board:")

       # Display the actual board
        for i in range(3):
            row = ""
            for j in range(3):
                pos = i * 3 + j
                row += f" {self.board[pos]} "
                if j < 2:
                    row += "|"
            print(row)
            if i < 2:
                print("-----------")
        print()

    def is_valid_move(self, position):
        """Check if the move is valid (position is empty and within range)."""
        try:
            pos = int(position) - 1  # Convert to 0-based index
            return 0 <= pos <= 8 and self.board[pos] == ' '
        except ValueError:
            return False

    def make_move(self, position):
        """Make a move on the board."""
        pos = int(position) - 1  # Convert to 0-based index
        self.board[pos] = self.current_player

    def check_winner(self):
        """Check if there's a winner or if the game is a draw."""
        # Define winning combinations (rows, columns, diagonals)
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]

        # Check each winning combination
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] ==
                self.board[combo[2]] != ' '):
                self.winner = self.board[combo[0]]
                self.game_over = True
                return True

        # Check for draw (board is full)
        if ' ' not in self.board:
            self.game_over = True
            self.winner = 'Draw'
            return True

        return False

    def switch_player(self):
        """Switch between X and O players."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_player_move(self):
        """Get and validate player input."""
        while True:
            try:
                move = input(f"Player {self.current_player}, enter your move (1-9): ").strip()

                if move.lower() in ['quit', 'exit', 'q']:
                    print("Thanks for playing!")
                    sys.exit()

                if self.is_valid_move(move):
                    return move
                else:
                    print("Invalid move! Please choose an empty position (1-9).")

            except KeyboardInterrupt:
                print("\nGame interrupted. Thanks for playing!")
                sys.exit()
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")

    def display_result(self):
        """Display the final result of the game."""
        self.display_board()
        print("="*30)
        if self.winner == 'Draw':
            print("     🤝 IT'S A DRAW! 🤝")
        else:
            print(f"   🎉 PLAYER {self.winner} WINS! 🎉")
        print("="*30)

    def play_game(self):
        """Main game loop."""
        print("Welcome to Tic-Tac-Toe!")
        print("Enter 'quit', 'exit', or 'q' anytime to quit the game.")
        input("Press Enter to start...")

        while not self.game_over:
            # Display current board
            self.display_board()

            # Get player move
            move = self.get_player_move()

            # Make the move
            self.make_move(move)

            # Check for winner or draw
            if self.check_winner():
                break

            # Switch to next player
            self.switch_player()

        # Display final result
        self.display_result()

def play_again():
    """Ask if players want to play another game."""
    while True:
        choice = input("\nWould you like to play again? (y/n): ").strip().lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def main():
    """Main function to run the game with replay option."""
    print("🎮 Welcome to the Ultimate Tic-Tac-Toe Game! 🎮")

    while True:
        # Create new game instance
        game = TicTacToe()

        # Play the game
        game.play_game()

        # Ask if players want to play again
        if not play_again():
            break

    print("\nThanks for playing Tic-Tac-Toe!")
    print("Visit our GitHub for more Python games and tutorials!")

# Game statistics and tips
def show_tips():
    """Display helpful tips for playing Tic-Tac-Toe."""
    tips = [
        "🎯 Tip 1: Try to get three in a row (horizontally, vertically, or diagonally)",
        "🎯 Tip 2: Block your opponent when they have two in a row",
        "🎯 Tip 3: Control the center (position 5) - it's the most strategic spot",
        "🎯 Tip 4: Corner positions (1, 3, 7, 9) are generally stronger than edges",
        "🎯 Tip 5: Think one move ahead - both offense and defense!"
    ]

    print("\n" + "="*50)
    print("           🎲 TIC-TAC-TOE STRATEGY TIPS 🎲")
    print("="*50)
    for tip in tips:
        print(tip)
    print("="*50)

# Additional feature: Show game rules
def show_rules():
    """Display the rules of Tic-Tac-Toe."""
    rules = """
    📋 GAME RULES:

    1. The game is played on a 3x3 grid
    2. Players take turns placing their mark (X or O)
    3. The first player to get 3 marks in a row wins
    4. Rows can be horizontal, vertical, or diagonal
    5. If all 9 squares are filled and no one wins, it's a draw
    6. Player X always goes first

    🎮 HOW TO PLAY:
    - Enter numbers 1-9 to choose your position
    - Type 'quit', 'exit', or 'q' to quit anytime
    - Follow the on-screen board layout for position reference
    """
    print(rules)

if __name__ == "__main__":
    # Show rules and tips before starting
    show_rules()
    show_tips()
    input("\nPress Enter to start playing...")

    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing! 👋")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please report this issue on our GitHub repository.")
