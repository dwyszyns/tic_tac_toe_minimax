import unittest
from Player import AIPlayer
from Board import Board


class TestAIPlayer(unittest.TestCase):
    def setUp(self):
        self.player = AIPlayer('x', 'AI', 9)

    def test_move(self):
        board = Board(3)
        board.board = [['o', 'x', 'o'],
                       [' ', 'x', ' '],
                       ['x', ' ', 'o']]
        self.player.move(board)
        self.assertEqual(board.board, [['o', 'x', 'o'],
                                       [' ', 'x', ' '],
                                       ['x', 'x', 'o']])

    def test_minimax(self):
        board = Board(3)
        board.board = [['o', 'x', 'x'],
                       ['x', 'x', ' '],
                       ['o', 'o', ' ']]

        value, move, _ = self.player.minimax(board, 3)

        self.assertEqual(value, 55)
        self.assertIn(move, [(1, 2)])


if __name__ == '__main__':
    unittest.main()
