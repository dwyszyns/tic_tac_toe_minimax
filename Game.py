from Board import Board
from Player import AIPlayer
from time import sleep


class Game:
    def __init__(self, board:Board, player1:AIPlayer, player2:AIPlayer):
        self.board = board
        self.player1 = player1
        self.player2 = player2

    def play(self):
        current_player = self.player1
        while (
            not self.board.check_winner() and len(self.board.get_available_moves()) > 0
        ):
            current_player.move(self.board)
            print(board)
            sleep(0.7)
            current_player = (
                self.player2 if current_player == self.player1 else self.player1
            )

    def print_game_result(self):
        winner = self.board.check_winner()
        if winner == self.player1.symbol:
            print(f"{self.player1.name} won!")
        elif winner is None:
            print("Draw")
        else:
            print(f"{self.player2.name} won!")


if __name__ == "__main__":
    board = Board(3)
    print("Starting game...")
    player1 = AIPlayer("x", "Dominika", 9)
    player2 = AIPlayer("o", "Wojtek", 1)
    game = Game(board, player1, player2)
    game.play()
    game.print_game_result()
