import tkinter as tk
from tkinter import simpledialog

class SOSGame:
    def __init__(self, root, board_size):
        self.root = root
        self.root.title("SOS Game")
        self.board_size = board_size
        self.current_player = 'S'

        # Initialize the board
        self.board = [[' ' for _ in range(board_size)] for _ in range(board_size)]

        # Create buttons for 'S' and 'O'
        self.s_button = tk.Button(root, text="S", command=lambda: self.place_symbol('S'))
        self.o_button = tk.Button(root, text="O", command=lambda: self.place_symbol('O'))

        # Create the board buttons using grid
        self.buttons = [[tk.Button(root, text='', width=4, height=2, command=lambda i=i, j=j: self.place_symbol_on_board(i, j)) for j in range(board_size)] for i in range(board_size)]

        # Pack buttons
        self.s_button.grid(row=board_size, column=0, columnspan=2)
        self.o_button.grid(row=board_size, column=2, columnspan=2)

        # Grid buttons
        for i in range(board_size):
            for j in range(board_size):
                self.buttons[i][j].grid(row=i, column=j)

    def place_symbol(self, symbol):
        self.current_player = symbol

    def place_symbol_on_board(self, row, col):
        if self.board_size > 0 and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            # Switch player
            self.current_player = 'S' if self.current_player == 'O' else 'O'

if __name__ == "__main__":
    # Get board size from the user
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    board_size = simpledialog.askinteger("Input", "Enter the board size (n x n):", initialvalue=5)

    if board_size is not None:
        root = tk.Tk()
        game = SOSGame(root, board_size)
        root.mainloop()
