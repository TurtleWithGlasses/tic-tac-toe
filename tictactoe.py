import tkinter as tk

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.buttons = []
        self.turn = True
        self.count = 0
        self.resizable(width=False, height=False)
        self.Board()



TicTacToe().mainloop()