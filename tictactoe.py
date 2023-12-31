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

    def Check_Results(self, char):
        if (((self.buttons[0][0]["text"] == char) and (self.buttons[0][1]["text"] == char) and (self.buttons[0][2]["text"] == char)) or
            ((self.buttons[1][0]["text"] == char) and (self.buttons[1][1]["text"] == char) and (self.buttons[1][2]["text"] == char)) or
            ((self.buttons[2][0]["text"] == char) and (self.buttons[2][1]["text"] == char) and (self.buttons[2][2]["text"] == char)) or
            ((self.buttons[0][0]["text"] == char) and (self.buttons[1][0]["text"] == char) and (self.buttons[2][0]["text"] == char)) or
            ((self.buttons[0][1]["text"] == char) and (self.buttons[1][1]["text"] == char) and (self.buttons[2][1]["text"] == char)) or
            ((self.buttons[0][2]["text"] == char) and (self.buttons[1][2]["text"] == char) and (self.buttons[2][2]["text"] == char)) or
            ((self.buttons[0][0]["text"] == char) and (self.buttons[1][1]["text"] == char) and (self.buttons[2][2]["text"] == char)) or
            ((self.buttons[0][2]["text"] == char) and (self.buttons[2][0]["text"] == char) and (self.buttons[1][1]["text"] == char))):
            self.Result(char)
        elif self.count == 9:
            self.Result("Draw")

    def Result(self, char):
        top = tk.Toplevel(self)
        if char == "Draw":
            top.title("Draw!")
            top_text = tk.Label(top, text="Game is a draw", font="Arial 30 bold", fg="blue")
        else:
            top.title("Congratulations!")
            top_text = tk.Label(top, text=f"{char} has won the game!", font="Arial 20 bold", fg="blue")

        top_button = tk.Button(top, text="New Game", bg="black", fg="white", activebackground="blue", activeforeground="green", command=self.New_Game)

        top_text.grid(row=0, column=0, padx=10, pady=19)
        top_button.grid(row=1, column=0)


TicTacToe().mainloop()