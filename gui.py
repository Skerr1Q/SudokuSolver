import tkinter as tk
import sudoku_solver as sds

class SudokuGUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Sudoku Solver")
        self.configure(bg = "#772F1A")

        try:
            self.img = tk.PhotoImage(file='C:\\Users\\Vlad Kostenko\\Desktop\\Folders\\Projects\\SudokuSolver\\icon.gif')
            self.tk.call('wm', 'iconphoto', self._w, self.img)
        except:
            pass

        self.geometry("600x700")
        self.resizable(0,0)
        
        self.frame = tk.Frame(self)
        self.frame.grid(padx = 25, pady = 30, columnspan = 2)

        #creates arrays of numbers, variables and entries
        self.create_empty_grid()
        self.var_grid = self.create_var_arr()
        self.cell_arr = self.create_cell_arr()

        #button that solves sudoku
        self.solve_btn = tk.Button(self, text = "Solve Sudoku", command = self.button_solve, bg="#585123", fg="white", font = ("times", 12))
        self.solve_btn.grid(ipady = 20, ipadx = 40, pady = 5, column = 0, row = 1)

        #button that clears grid
        self.clear_btn = tk.Button(self, text = "Clear the board", command = self.create_empty_grid, bg="#585123", fg="white", font = ("times", 12))
        self.clear_btn.grid(ipady = 20, ipadx = 40, pady = 5, column = 1, row = 1)

    #function to clear grid
    def create_empty_grid(self):
        self.start_grid = [[0 for x in range(9)] for y in range(9)]

        #updates var_grid if start_grid is cleared, else passes
        try:
            self.update_grid()
        except:
            pass

    #creates empty sudoku grid
    def create_cell_arr(self):

        cell_arr = []
        #fills array of cells
        for i in range(9):
            cell_vect = []
            for j in range(9):
                cell = tk.Entry(self.frame,  textvariable = self.var_grid[i][j], width =7, font = ("times", 12), justify = "center", bd=2, fg="white",\
                                bg="#F58549" if (i in range(3, 6)) ^ (j in range(3, 6)) else "#F2A65A").grid(ipady = 16,  row = i, column = j)
                cell_vect.append(cell)
            cell_arr.append(cell_vect)
        
        return cell_arr

    #create array of IntVar
    def create_var_arr(self):
        var_arr = []
        for i in range(9):
            var_vec = []
            for j in range(9):
                var = tk.IntVar(self, value = self.start_grid[i][j])
                var.trace_add("write", callback=lambda *args, varv=var, i=i, j=j: self.validate_input(varv, i, j))
                var_vec.append(var)
            var_arr.append(var_vec) 

        return var_arr

    #function for button
    def button_solve(self):
        #self.update_start_arr()
        test_grid = self.start_grid.copy()
        if sds.solve_sudoku(test_grid):
            self.start_grid = test_grid
            self.update_grid()
        else:
            tk.messagebox.showwarning(title="Sudoku Solver", message="This sudoku is unsolvable")
            self.create_empty_grid()
            self.update_grid()

    #updates grid
    def update_grid(self):
        for i in range(9):
            for j in range(9):
                self.var_grid[i][j].set(self.start_grid[i][j])

    #function that validates input
    def validate_input(self, num, i, j):
        try:
            if num:
                list_num = list(str(num.get()))
                num.set(int(list_num[-1]))
        except: 
            num.set(0)
        self.start_grid[i][j] = num.get()

if __name__=="__main__":

    root = SudokuGUI()
    root.mainloop()