import tkinter as tk
import sudoku_solver as sds

class SudokuGUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Sudoku Solver")
        self.configure(bg = "#772F1A")
        self.geometry("600x700")
        self.resizable(0,0)
        
        self.frame = tk.Frame(self)
        self.frame.grid(padx = 25, pady = 30, columnspan = 2)

        #creates arrays of numbers, variables and entries
        self.create_empty_grid()
        self.update_grid()

        #button that solves sudoku
        self.solve_btn = tk.Button(self, text = "Solve Sudoku", command = self.button_solve, bg="#585123", fg="white", font = ("times", 12))
        self.solve_btn.grid(ipady = 20, ipadx = 40, pady = 5, column = 0, row = 1)

        #button that clears grid
        self.clear_btn = tk.Button(self, text = "Clear the board", command = self.create_empty_grid, bg="#585123", fg="white", font = ("times", 12))
        self.clear_btn.grid(ipady = 20, ipadx = 40, pady = 5, column = 1, row = 1)

    #function to clear grid
    def create_empty_grid(self):
        self.start_grid = [[0 for x in range(9)] for y in range(9)]
        self.update_grid()

    #creates empty sudoku grid
    def create_arr(self):

        cell_arr = []
        #fills array of cells
        for i in range(9):
            cell_vect = []
            for j in range(9):
                cell = tk.Entry(self.frame,  textvariable = self.var_grid[i][j], width =7, font = ("times", 12), justify = "center", bd=2, fg="white",\
                                bg="#F58549" if (i in range(3, 6)) ^ (j in range(3, 6)) else "#F2A65A")
                cell_vect.append(cell)
            cell_arr.append(cell_vect)
        
        #places cells on screen
        for i in range(9):
            for j in range(9):
                cell_arr[i][j].grid(ipady = 16,  row = i, column = j)

        return cell_arr

    #create array of IntVar
    def create_var_arr(self):
        var_arr = []
        for i in range(9):
            var_vec = []
            for j in range(9):
                var = tk.IntVar(self, value = self.start_grid[i][j])
                var_vec.append(var)
            var_arr.append(var_vec) 

        return var_arr

    #function for button
    def button_solve(self):
        self.update_start_arr()
        if sds.solve_sudoku(self.start_grid):
            self.update_grid()

    def update_start_arr(self):
        self.start_grid = [[var.get() for var in vect] for vect in self.var_grid]

    #updates grid
    def update_grid(self):

        self.var_grid = self.create_var_arr()
        self.cell_arr = self.create_arr()

if __name__=="__main__":

    root = SudokuGUI()
    root.mainloop()

