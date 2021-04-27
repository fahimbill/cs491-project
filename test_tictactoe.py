import unittest
from tictactoe import Board


class TicTacToeUnitTesting (unittest.TestCase):

    def setUp(self):
        self.Board = Board()


    def test_valid(self):
        board = Board()
        board.mark_square(0, 1, 's')
        self.assertIsNot(board.board[0][1], 'x')

    def test_mark_square(self):
        board = Board()
        board.mark_square(0, 0, 'X')
        self.assertEqual(board.board[0][0], 'X')



    def test_legal_move(self):
        self.assertEqual(self.Board.check_valid(1, 1), True)

    def test_illegal_move_row(self):
        self.assertEqual(self.Board.check_valid(4, 0), False)

    def test_illegal_move_column(self):
        self.assertEqual(self.Board.check_valid(0, 4), False)

    def test_illegal_move_neg_row(self):
        self.assertEqual(self.Board.check_valid(-1, 0), False)

    def test_illegal_move_neg_column(self):
        self.assertEqual(self.Board.check_valid(0, -1), False)

    def test_illegal_move_both(self):
        self.assertEqual(self.Board.check_valid(4, 4), False)

    def test_illegal_move_neg_both(self):
        self.assertEqual(self.Board.check_valid(-1, -1), False)

    def test_vertical_winner(self):
        self.Board.mark_square(1, 0, "X")
        self.Board.mark_square(0, 2, "O")
        self.Board.mark_square(1, 1, "X")
        self.Board.mark_square(0, 1, "O")
        self.Board.mark_square(1, 2, "X")
        print("Vertical Test:")
        self.Board.print_board()
        print("\n")
        self.assertEqual(self.Board.has_winner(), True, "Unit pass for vertical")

    def test_horizontal_winner(self):
        self.Board.mark_square(0, 1, "X")
        self.Board.mark_square(0, 2, "O")
        self.Board.mark_square(1, 1, "X")
        self.Board.mark_square(1, 2, "O")
        self.Board.mark_square(2, 1, "X")
        print("Horizontal Test:")
        self.Board.print_board()
        print("\n")
        self.assertEqual(self.Board.has_winner(), True, "Unit pass for horizontal")

    def test_diagonal_winner(self):
        self.Board.mark_square(0, 0, "X")
        self.Board.mark_square(1, 0, "0")
        self.Board.mark_square(1, 1, "X")
        self.Board.mark_square(0, 2, "0")
        self.Board.mark_square(2, 2, "X")
        print("Diagonal Test:")
        self.Board.print_board()
        print("\n")
        self.assertEqual(self.Board.has_winner(), True, "Unit pass for diagonal")



    def player_switch_X(self):
        self.Board.mark_square(0, 0, "X")
        self.Board.mark_square(0, 1, "X")
        self.assertIsNot(self.Board.mark_square(0, 1, "X"), self.Board.mark_square(0, 1, "O"))

    def player_switch_0(self):
        self.Board.mark_square(1, 0, "O")
        self.Board.mark_square(1, 1, "O")
        self.assertIsNot(self.Board.mark_square(1, 1, "O"), self.Board.mark_square(1, 1, "X"))








if __name__ == '__main__':
    unittest.main()