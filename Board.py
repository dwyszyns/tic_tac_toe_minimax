class Board:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [[" " for _ in range(board_size)] for _ in range(board_size)]

    def check_row(self, row: int) -> str | None:
        value = self.board[row][0]
        return (
            value if value != " " and all(
                self.board[row][column] == value for column in range(self.board_size)
            )
            else None
        )

    def check_rows(self) -> str | None:
        return next(
            (
                self.check_row(row)
                for row in range(self.board_size)
                if self.check_row(row) is not None
            ),
            None,
        )

    def check_column(self, column: int) -> str | None:
        value = self.board[0][column]
        return (
            value if value != " " and all(
                row[column] == value for row in self.board
            )
            else None
        )

    def check_columns(self) -> str | None:
        return next(
            (
                self.check_column(column)
                for column in range(self.board_size)
                if self.check_column(column) is not None
            ),
            None,
        )

    def check_diagonal(self) -> str | None:
        value = self.board[0][0]
        if value != " " and all(
            self.board[coord][coord] == value for coord in range(self.board_size)
        ):
            return value
        value = self.board[0][self.board_size - 1]
        if value != " " and all(
            self.board[coord][self.board_size - 1 - coord] == value
            for coord in range(self.board_size)
        ):
            return value
        return None

    def check_winner(self) -> str | None:
        checks = [self.check_rows(), self.check_columns(), self.check_diagonal()]
        return next((result for result in checks if result is not None), None)

    def __str__(self):
        s = (4 * self.board_size + 1) * "-" + "\n"
        for row in self.board:
            s += "|"
            for elem in row:
                s += f" {elem} |"
            s += "\n" + (4 * self.board_size + 1) * "-" + "\n"
        return s

    def game_over(self) -> bool:
        return " " not in [elem for row in self.board for elem in row]

    def get_available_moves(self) -> list:
        return [
            (row, col)
            for row in range(self.board_size)
            for col in range(self.board_size)
            if self.board[row][col] == " "
        ]

    def generate_price_board(self) -> list:
        price_board = [
            [0 for _ in range(self.board_size)] for _ in range(self.board_size)
        ]
        for i in range(self.board_size):
            for j in range(self.board_size):
                if i == j or i + j == self.board_size - 1:
                    price_board[i][j] = 3
                else:
                    price_board[i][j] = 2
        if self.board_size % 2 != 0:
            price_board[self.board_size // 2][self.board_size // 2] = 4
        return price_board
