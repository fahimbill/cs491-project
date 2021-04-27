from tictactoe import *


class Player:

    def __init__(self, board):
        self.board = board
        self.player = "X"

    def play_game(self):

        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends
        :return: (str) the letter representing the player who won
        """

        while self.board.has_winner() == False:
            print("It's " + self.player + "'s turn.")
            row = input("Enter a row\n")
            col = input("Enter a column\n")

            if not self.board.check_valid(int(row), int(col)):
                print("Please try again")

            else:
                self.player = self.board.mark_square(int(col), int(row), self.player)
                self.board.print_board()

        return self.player


