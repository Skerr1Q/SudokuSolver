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

        
        self.test_grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
                    [5, 2, 0, 0, 0, 0, 0, 0, 0],
                    [0, 8, 7, 0, 0, 0, 0, 3, 1],
                    [0, 0, 3, 0, 1, 0, 0, 8, 0],
                    [9, 0, 0, 8, 6, 3, 0, 0, 5],
                    [0, 5, 0, 0, 9, 0, 6, 0, 0],
                    [1, 3, 0, 0, 0, 0, 2, 5, 0],
                    [0, 0, 0, 0, 0, 0, 0, 7, 4],
                    [0, 0, 5, 2, 0, 6, 3, 0, 0]]

        self.update()

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
                cell = tk.Entry(self.frame, state=tk.DISABLED, textvariable = self.var_grid[i][j], width =10, justify = "center", bd=2,)
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
                var = tk.IntVar(self, value = self.test_grid[i][j])
                var_vec.append(var)
            var_arr.append(var_vec) 

        return var_arr

    #function for button
    def button_solve(self):
        sds.solve_sudoku(self.test_grid)
        self.update()

    #updates grid
    def update(self):

        self.var_grid = self.create_var_arr()
        self.cell_arr = self.create_arr()

if __name__=="__main__":

    root = SudokuGUI()
    root.mainloop()

