import tkinter as tk
import sudoku_solver as sds

class SudokuGUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Sudoku Solver")
        self.geometry("600x700")
        self.resizable(0,0)
        
        self.frame = tk.Frame(self)
        self.frame.grid()

        
        self.start_grid = [[0 for x in range(9)] for y in range(9)]
        #array of IntVars
        self.var_grid = self.create_var_arr()
        #array of entries
        self.cell_arr = self.create_arr()

        #button that solves sudoku
        self.solve_btn = tk.Button(self, text = "Solve Sudoku", command = self.button_solve)
        self.solve_btn.grid(ipady = 20, ipadx = 40, pady = 20)


    #creates empty sudoku grid
    def create_arr(self):

        cell_arr = []
        #fills array of cells
        for i in range(9):
            cell_vect = []
            for j in range(9):
                cell = tk.Entry(self.frame,  textvariable = self.var_grid[i][j], width =10, justify = "center", bd=2,)
                cell_vect.append(cell)
            cell_arr.append(cell_vect)
        
        #places cells on screen
        for i in range(9):
            for j in range(9):
                cell_arr[i][j].grid(ipady = 20,  row = i, column = j)

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
        sds.solve_sudoku(self.start_grid)
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

