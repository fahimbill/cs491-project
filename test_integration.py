import unittest
from unittest.mock import patch
from tictactoe import Board
from player import Player


class TicTacToeUnitTesting(unittest.TestCase):

    def setUp(self):
        self.Board = Board()
        self.Player = Player(self.Board)

    def test_no_winner(self):
        self.Board = Board()
        self.Player = Player(self)
        self.Board.mark_square(0, 0, "X")
        self.Board.mark_square(0, 1, "0")
        self.Board.mark_square(0, 2, "X")
        self.Board.mark_square(1, 0, "0")
        self.Board.mark_square(1, 1, "X")
        self.Board.mark_square(1, 2, "0")
        self.Board.mark_square(2, 1, "X")
        self.Board.mark_square(2, 2, "0")
        print("No Winner Test:")
        self.Board.print_board()
        print("\n")
        self.assertEqual(self.Board.has_winner(), True, "Unit pass for no winner")





    @patch('builtins.input', side_effect=['0', '0', '0', '1', '1', '1', '2', '1', '2', '2'])
    def test_play_game(self, mock_input):
        self.Player.play_game()
        assert (self.Board.has_winner())




if __name__ == '__main__':
    unittest.main()