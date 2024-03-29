from cmath import inf
from Board import Board
import random


class AIPlayer:
    def __init__(self, symbol: str, name: str, depth: int):
        self.symbol = symbol
        self.name = name
        self.depth = depth

    def move(self, board: Board):
        value, move, _ = self.minimax(board, self.depth, True)
        print(f"Chosen: {value} {move}")
        board.board[move[0]][move[1]] = self.symbol

    def evaluate(self, board: Board) -> int:
        price_board = board.generate_price_board()
        price = 0
        opponent_symbol = "x" if self.symbol == "o" else "o"
        for i in range(board.board_size):
            for j in range(board.board_size):
                if board.board[i][j] == self.symbol:
                    price += price_board[i][j]

                elif board.board[i][j] == opponent_symbol:
                    price -= price_board[i][j]

        if board.check_winner() == self.symbol:
            price += 50

        elif board.check_winner() == opponent_symbol:
            price -= 50

        return price

    def check_best_move_condition(
        self, current_value, value, current_depth, best_depth, maximizing_player
    ):
        if maximizing_player:
            return current_value > value or (
                current_value == value and current_depth < best_depth
            )
        else:
            return current_value < value or (
                current_value == value and current_depth < best_depth
            )

    def minimax(self, board: Board, depth: int, maximizing_player: bool = True):
        if depth == 0 or board.game_over() or board.check_winner() is not None:
            return self.evaluate(board), None, depth

        available_moves = board.get_available_moves()
        best_moves = []
        best_depth = float("inf")
        value = float("-inf") if maximizing_player else float("inf")
        best_move = None
        opponent_symbol = "o" if self.symbol == "x" else "x"
        for move in available_moves:
            board.board[move[0]][move[1]] = (
                self.symbol if maximizing_player else opponent_symbol
            )
            current_value, _, current_depth = self.minimax(
                board, depth - 1, not maximizing_player
            )
            board.board[move[0]][move[1]] = " "
            if self.check_best_move_condition(
                current_value, value, current_depth, best_depth, maximizing_player
            ):
                value = current_value
                best_move = move
                best_moves = [best_move]
            elif current_value == value:
                best_moves.append(move)

        return value, random.choice(best_moves), best_depth
