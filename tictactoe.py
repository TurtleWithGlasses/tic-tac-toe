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

    def Turn_Taken(self, x, y):
        self.count += 1
        if self.turn:
            char = "X"
            self.buttons[x][y].config(text="X", bg="black", state="disabled")
        else:
            char = "O"
            self.buttons[x][y].config(text="O", bg="light gray", state="disabled")
        self.Check_Results(char)
        self.turn = not self.turn


    def New_Game(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.buttons = []
        self.turn = True
        self.count = 0
        self.Board()


    def Check_Results(self):
        pass


TicTacToe().mainloop()