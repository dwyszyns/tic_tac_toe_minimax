import unittest
from Player import AIPlayer
from Board import Board


class TestAIPlayer(unittest.TestCase):
    def setUp(self):
        self.player = AIPlayer('x', 'AI', 9, True)

    def test_move(self):
        # Create a board with some initial state
        board = Board(3)
        board.board = [['o', 'x', 'o'],
                       [' ', 'x', ' '],
                       ['x', ' ', 'o']]
        # Call the move method
        self.player.move(board)
        print(board.board)
        # Check if the move was made correctly
        self.assertEqual(board.board, [['o', 'x', 'o'],
                                       [' ', 'x', ' '],
                                       ['x', 'x', 'o']])

    def test_minimax(self):
        # Create a board with some state
        board = Board(3)
        board.board = [['o', 'x', 'x'],
                       ['x', 'x', ' '],
                       ['o', 'o', ' ']]

        # Call the minimax method
        value, move, _ = self.player.minimax(board, 3, True)

        # Check if the returned value and move are correct

        self.assertEqual(value, 55)
        self.assertIn(move, [(1, 2)])


if __name__ == '__main__':
    unittest.main()
