from cmath import inf
import random


class Player:
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name

    def move(self, board):
        while True:
            try:
                print(f"{self.name}, it's your turn. Enter row and column (comma-separated): ")
                row, column = map(int, input().split(' '))
                row -= 1
                column -= 1
                if 0 <= row < len(board.board) and 0 <= column < len(board.board[0]) and board.board[row][column] == ' ':
                    board.board[row][column] = self.symbol
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter two integers separated by a comma.")
            except IndexError:
                print("Invalid input. Row and column must be within the board.")


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
        price_board = [[3, 2, 3],
                       [2, 4, 2],
                       [3, 2, 3]]

        oponent_sum = 0
        player_sum = 0
        oponent_symbol = 'x' if self.symbol == 'o' else 'o'
        for i in range(len(board.board)):
            for j in range(len(board.board[0])):
                if board.board[i][j] == self.symbol:
                    player_sum += price_board[i][j]

                elif board.board[i][j] == oponent_symbol:
                    oponent_sum += price_board[i][j]

        if board.check_winner() == self.symbol:
            player_sum += 50

        elif board.check_winner() == oponent_symbol:
            oponent_sum += 50

        return player_sum - oponent_sum

    def minimax(self, board, depth, maximizing_player=True):
        if depth == 0 or board.game_over() or board.check_winner() is not None:
            return self.evaluate(board), None, depth

        available_moves = board.get_available_moves()
        best_moves = []
        best_depth = float('inf')
        if maximizing_player:
            value = float('-inf')
            best_move = None
            for move in available_moves:
                board.board[move[0]][move[1]] = self.symbol
                current_value, _, current_depth = self.minimax(board, depth - 1, False)
                board.board[move[0]][move[1]] = ' '
                if current_value > value or (current_value == value and current_depth < best_depth):
                    value = current_value
                    best_move = move
                    best_moves = [best_move]
                elif current_value == value:
                    best_moves.append(move)
        else:
            value = float('inf')
            best_move = None
            for move in available_moves:
                board.board[move[0]][move[1]] = 'o' if self.symbol == 'x' else 'x'
                current_value, _, current_depth = self.minimax(board, depth - 1, True)
                board.board[move[0]][move[1]] = ' '  
                if current_value < value or (current_value == value and current_depth < best_depth):
                    value = current_value
                    best_move = move
                    best_moves = [best_move]
                elif current_value == value:
                    best_moves.append(move)

        return value, random.choice(best_moves), best_depth
    

  
    