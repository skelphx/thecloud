import random
import os
import sys

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'
        self.game_over = False
        self.winner = None

    def display_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nTic-Tac-Toe\n")
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
        try:
            pos = int(position) - 1
            return 0 <= pos <= 8 and self.board[pos] == ' '
        except ValueError:
            return False

    def make_move(self, position):
        pos = int(position) - 1
        self.board[pos] = self.current_player

    def check_winner(self):
        combos = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
        for combo in combos:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                self.winner = self.board[combo[0]]
                self.game_over = True
                return True
        if ' ' not in self.board:
            self.winner = 'Draw'
            self.game_over = True
            return True
        return False

 def switch_player(self):
         self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_move(self):
      if self.current_player == 'X':
         while True:
             move = input("Your move (1–9): ")
             if move.lower() in ['q', 'quit', 'exit']:
                 sys.exit("Game exited.")
             if self.is_valid_move(move):
                 return move
             print("Invalid. Try again.")
      else:
         available = [str(i+1) for i, val in enumerate(self.board) if val == ' ']
         move = random.choice(available)
         print(f"AI chooses: {move}")
         return move

    def play(self):
        input("Press Enter to begin...")
        while not self.game_over:
            self.display_board()
            move = self.get_move()
            self.make_move(move)
            if self.check_winner():
                break
            self.switch_player()
        self.display_board()
        print(f"🎉 Result: {self.winner}!")

def main():
    while True:
        game = TicTacToe()
        game.play()
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()
