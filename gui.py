import tkinter as tk

class SudokuGUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Sudoku Solver")
        self.geometry("600x700")
        self.resizable(0,0)

        self.frame = tk.Frame(self)
        self.frame.grid()
        self.create_arr()

        #button that solves sudoku
        self.solve_btn = tk.Button(self, text = "Solve Sudoku", command = self.solve())
        self.solve_btn.grid(ipady = 20, ipadx = 40, pady = 20)


    #creates empty sudoku grid
    def create_arr(self):

        cell_arr = []
        #fills array of cells
        for i in range(9):
            cell_vect = []
            for j in range(9):
                cell = Cell(self.frame, 0)
                cell_vect.append(cell)
            cell_arr.append(cell_vect)
        
        #places cells on screen
        for i in range(9):
            for j in range(9):
                cell_arr[i][j].entry.grid(ipady = 20,  row = i, column = j)

        return cell_arr

    #solves sudoku using backtracking
    def solve(self):
        pass

    #draws cells in sudoku
    def draw(self):
        pass

# cell in sudoku
class Cell():

    def __init__(self, root, num):
        self.var = tk.IntVar(root, value = num)
        self.entry = tk.Entry(root, width =10, justify = "center", bd=2,  textvariable = self.var)

if __name__=="__main__":

    root = SudokuGUI()
    root.mainloop()

