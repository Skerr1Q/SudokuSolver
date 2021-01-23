import tkinter as tk

#creating GUI
class SudokuGUI(tk.Tk):
    def __init__(self, root):

        self.root = root
        root.title("Sudoku Solver")
        root.geometry('600x700')

        self.solve_button = tk.Button(root, text ="Solve Sudoku", command = self.solve())
        self.solve_button.grid(padx=120, pady = 30, side = "bottom")

    # creating cells on the board
    def create(self)

        for i in range(9):
            for j in range(9):



    def solve(self):
        pass

#cell class deriving from tk.Entry
class Cell(tk.Entry):
    def __init__(self, root, row, col, num):
        super().__init__(root)
        self.row = row
        self col = col
        self.num = num

        num = tk.IntVar()
        self.grid(row = row, column = col, text_variable = num)


if __name__ = "__main__":
    root = tk.Tk()
    my_gui = SudokuGUI(root)
    root.mainloop()
    c = Cell()