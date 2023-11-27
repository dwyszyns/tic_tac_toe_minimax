from cmath import inf
import random

warunki = {
    True: lambda current_value, value, current_depth, best_depth: current_value > value
    or (current_value == value and current_depth < best_depth),
    False: lambda current_value, value, current_depth, best_depth: current_value < value
    or (current_value == value and current_depth < best_depth),
}

class AIPlayer:
    def __init__(self, symbol, name, depth):
        self.symbol = symbol
        self.name = name
        self.depth = depth

    def move(self, board):
        val, move, _ = self.minimax(board, self.depth, True)
        print(f"Chosen: {val} {move}")
        board.board[move[0]][move[1]] = self.symbol

    def evaluate(self, board):
        price_board = board.generate_price_board()
        price = 0
        oponent_symbol = "x" if self.symbol == "o" else "o"
        for i in range(len(board.board)):
            for j in range(len(board.board[0])):
                if board.board[i][j] == self.symbol:
                    price += price_board[i][j]

                elif board.board[i][j] == oponent_symbol:
                    price -= price_board[i][j]

        if board.check_winner() == self.symbol:
            price += 50

        elif board.check_winner() == oponent_symbol:
            price -= 50

        return price

    def minimax(self, board, depth, maximizing_player=True):
        if depth == 0 or board.game_over() or board.check_winner() is not None:
            return self.evaluate(board), None, depth

        available_moves = board.get_available_moves()
        best_moves = []
        best_depth = float("inf")
        value = float("-inf") if maximizing_player else float("inf")
        best_move = None
        opponent_symbol = "o" if self.symbol == "x" else "x"
        for move in available_moves:
            board.board[move[0]][move[1]] = (self.symbol if maximizing_player else opponent_symbol)
            current_value, _, current_depth = self.minimax(board, depth - 1, not maximizing_player)
            board.board[move[0]][move[1]] = " "
            if warunki[maximizing_player](
                current_value, value, current_depth, best_depth
            ):
                value = current_value
                best_move = move
                best_moves = [best_move]
            elif current_value == value:
                best_moves.append(move)

        return value, random.choice(best_moves), best_depth
