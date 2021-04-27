from player import *
""" Note: Although the skeleton below is in Python, you may use any programming language you want so long as the language supports object-oriented programming, 
          and you make use of relevant object-oriented design principles.
"""


class Board(object):

    def __init__(self):
        """
        Initializes the Board of size 3x3
        """
        self.board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        self.count = 0

        pass


    def has_winner(self):
        """
        Checks to see if there is a current winner of the game
        :return: ????
        """

        win = False
        # horizontal wins
        for x in range(0, 3):
            if self.board[x][0] != '_' and self.board[x][0] == self.board[x][1] and self.board[x][1] == self.board[x][2]:
                win = True

        for y in range(0, 3):
            if self.board[0][y] != '_' and self.board[0][y] == self.board[1][y] and self.board[1][y] == self.board[2][y]:
                win = True

        # vertical wins
        if self.board[0][0] != '_' and self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]:
            win = True

        if self.board[0][2] != '_' and self.board[0][2] == self.board[1][1] and self.board[2][0] == self.board[1][1]:
            win = True

        if self.count == 8:
            win = True

        return win

        pass

    def mark_square(self, column, row, player):
        """
        Marks a square at coordinate (column, row) for player
        :param column: (int) the 0-indexed column of the Board to mark
        :param row: (int) the 0-indexed row of the Board to mark
        :param player: (str) the X or O representation of which player to mark in square
        :return: ????
        """
        new_player = " "
        if (player == "X"):
            self.board[row][column] = 'X'
            new_player = "O"
            self.count = self.count + 1

        else:
            self.board[row][column] = 'O'
            new_player = "X"
            self.count = self.count + 1

        if (self.has_winner() == True and new_player == "X"):
            new_player = "O"
        elif (self.has_winner() == True and new_player == "O"):
            new_player = "X"

        return new_player


    def check_valid(self, row, col):
        if (col >= 0 and col <= 2 and row >= 0 and row <= 2) and (self.board[row][col] != "X") and (self.board[row][col] != "O"):
            return True
        else:
            return False
        pass

    def print_board(self):
        for x in range(0, 3):
            print(self.board[x])


if __name__ == '__main__':
    board = Board()
    player = Player(board)
    winner = player.play_game()
    print("{} has won!".format(winner))