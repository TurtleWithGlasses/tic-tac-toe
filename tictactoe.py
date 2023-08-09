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

    def Board(self):
        for i in range(0, 3):
            row = []
            for j in range(0, 3):
                row.append(tk.Button(self, width=10, height=3, font="Arial 35 bold",
                                     command=lambda x=i, y=j: self.Turn_Taken(x, y)))
                row[j].grid(row=i, column=j)
            self.buttons.append(row)
        tk.Button(self, text="New Game", width=10, height=1, font="Arial 35 bold",
                  bg="black", fg="gray", activeforeground="white", activebackground="blue",
                  command=self.New_Game).grid(row=3, column=1)




TicTacToe().mainloop()