import random as ran
import tkinter as tk
import tkinter.messagebox
from itertools import chain
#####################################################################################################################################
def merge(array, direction):
    '''
    For this assignment, you will implement a function merge(line) that models
    the process of merging all of the tile values in a single row or column.
    This function takes the list line as a parameter and returns a new list with
    the tile values from line slid towards the front of the list and merged.
    Note that you should return a new list and you should not modify the input
    list. This is one of the more challenging parts of implementing the game.

    In this function, you are always sliding the values in the list towards the
    front of the list (the list position with index 0). You will make sure you
    order the entries in line appropriately when you call this function later in
    the next assignment. Empty grid squares with no displayed value will be
    assigned a value of zero in our representation.

    As you work on your merge function, here are some simple tests you should try:

    [2, 0, 2, 4] should return [4, 4, 0, 0]
    [0, 0, 2, 2] should return [4, 0, 0, 0]
    [2, 2, 0, 0] should return [4, 0, 0, 0]
    [2, 2, 2, 2, 2] should return [4, 4, 2, 0, 0]
    [8, 16, 16, 8] should return [8, 32, 8, 0]
    '''
    if direction == 'Left' or direction == 'Up' or direction == 'Down':
        merge_array = []
        taken = []
        for ind in range(len(array)):
            if ind not in taken:
                if array[ind] in array[ind+1:] and array[ind] != 0:
                    for itr in range(ind+1, len(array)):
                        if array[itr] == array[ind] and array[itr] != 0:
                            merge_array.append(array[ind]*2)
                            taken.append(ind)
                            taken.append(itr)
                            break
                        else:
                            if array[itr] != 0:
                                merge_array.append(array[ind])
                                taken.append(ind)
                                break
                else:
                    if array[ind] != 0:
                        merge_array.append(array[ind])
                        taken.append(ind)
        return merge_array+[0]*(len(array)-len(merge_array))
    elif direction == 'Right':
        merge_array = []
        taken = []
        Array = array.copy()
        Array.reverse()
        for ind in range(len(array)):
            if ind not in taken:
                if Array[ind] in Array[ind+1:] and Array[ind] != 0:
                    for itr in range(ind+1, len(Array)):
                        if Array[itr] == Array[ind] and Array[itr] != 0:
                            merge_array.append(Array[ind]*2)
                            taken.append(ind)
                            taken.append(itr)
                            break
                        else:
                            if Array[itr] != 0:
                                merge_array.append(Array[ind])
                                taken.append(ind)
                                break
                else:
                    if Array[ind] != 0:
                        merge_array.append(Array[ind])
                        taken.append(ind)
        merge_array.reverse()
        return [0]*(len(array)-len(merge_array))+ merge_array  
#####################################################################################################################################
global game_grid
class Full_2048:
    def __init__(self, rows, cols):
        '''
        This function is used to initiate the game
        '''
        self.rows = rows
        self.cols = cols
        self.GUI = tk.Tk()
        self.GUI.title('2048')
        self.Menu()
        self.generate_game_at_first(rows, cols)
        self.game_grid(rows,cols)
        self.GUI.bind("<Key>", self.key)
        self.GUI.mainloop()

    def generate_game_at_first(self, rows, cols):
        '''
        This function is used to initiate the game grid
        '''
        global game_grid, thelabel, change
        start = 0
        game_grid = [[0 for i in range(cols)] for j in range(rows)]
        thelabel = [[tk.Label(self.GUI, text = '', bg = 'silver', fg = 'black',
                     borderwidth=5, relief="solid") for i in range(cols)] for j in range(rows)]
        while start < 2 :
            rand = ran.random()
            rand_row = ran.randint(0,self.rows-1)
            rand_col = ran.randint(0,self.cols-1)
            if rand <= 0.9 and game_grid[rand_row][rand_col] == 0:
                game_grid[rand_row][rand_col] = 2
                start += 1
            elif rand > 0.9 and game_grid[rand_row][rand_col] == 0:
                game_grid[rand_row][rand_col] = 4
                start += 1
            change = 1
    
    def game_grid(self, rows, cols):
        '''
        This function is used to draw 2048 element
        '''
        global game_grid, thelabel, change
        
        game_grid_width = 7
        game_grid_height = 3
        bg_colors = {0:'silver', 2:'darksalmon', 4:'coral',8:'sandybrown', 16:'orange', 32:'red',
                     64:'royalblue', 128:'purple', 256:'gold', 512:'crimson',1024:'seagreen', 2048:'green'}
        if change == 1:
            for row in range(rows):
                for col in range(cols):
                    if game_grid[row][col] == 0:
                        thelabel[row][col].destroy()
                        thelabel[row][col] = tk.Label(self.GUI, text = '',
                                            bg = bg_colors[game_grid[row][col]], fg = 'black',
                                            borderwidth=5, relief="solid")
                        thelabel[row][col].config(height=game_grid_height, width=game_grid_width, font=('Arial', 0, 'bold'))
                        thelabel[row][col].grid(row=str(row), column = str(col))
                    else:
                        thelabel[row][col].destroy()
                        thelabel[row][col] = tk.Label(self.GUI, text = str(game_grid[row][col]),
                                            bg = bg_colors[game_grid[row][col]], fg = 'black',
                                            borderwidth=5, relief="solid")
                        thelabel[row][col].config(height=game_grid_height, width=game_grid_width, font=('Arial', 0, 'bold'))
                        thelabel[row][col].grid(row=str(row), column = str(col))
            change = 0

    def add_new(self):
        '''
        This function is used to add new element to game_grid
        '''
        global game_grid
        add = 0
        while add < 1:
            rand = ran.random()
            rand_row = ran.randint(0,self.rows-1)
            rand_col = ran.randint(0,self.cols-1)
            if rand <= 0.9 and game_grid[rand_row][rand_col] == 0:
                game_grid[rand_row][rand_col] = 2
                add += 1
            elif rand > 0.9 and game_grid[rand_row][rand_col] == 0:
                game_grid[rand_row][rand_col] = 4
                add += 1
        
    def key(self,event):
        '''
        This function is used to return the entered key
        '''
        global game_grid, change
        game_grid_copy = game_grid.copy()
        if str(event.keysym) == 'Left':
            for row in range(self.rows):
                game_grid[row] = merge(game_grid[row], str(event.keysym))
            if game_grid != game_grid_copy:
                change = 1
                self.add_new()
                self.game_grid(self.rows, self.cols)
        elif str(event.keysym) == 'Up':
            game_grid = list(map(list, zip(*game_grid)))
            for col in range(self.cols):
                game_grid[col] = merge(game_grid[col], str(event.keysym))
            game_grid = list(map(list, zip(*game_grid)))
            if game_grid != game_grid_copy:
                change = 1
                self.add_new()
                self.game_grid(self.rows, self.cols)
        elif str(event.keysym) == 'Right':
            for row in range(self.rows):
                game_grid[row] = merge(game_grid[row], str(event.keysym))
            if game_grid != game_grid_copy:
                change = 1
                self.add_new()
                self.game_grid(self.rows, self.cols)
        elif str(event.keysym) == 'Down':
            game_grid = list(map(list, zip(*game_grid)))
            for col in range(self.cols):
                game_grid[col].reverse()
                game_grid[col] = merge(game_grid[col], str(event.keysym))
                game_grid[col].reverse()
            game_grid = list(map(list, zip(*game_grid)))
            if game_grid != game_grid_copy:
                change = 1
                self.add_new()
                self.game_grid(self.rows, self.cols)
        self.end_game()
        
    def end_game(self):
        '''
        This function is used to check the end of the game
        '''
        global game_grid
        if self.check_end():
            answer = tkinter.messagebox.askquestion('Game Over !', 'Do you play a new game ?')
            if answer == 'yes':
                self.generate_game_at_first(self.rows, self.cols)
                self.game_grid(self.rows, self.cols)
            elif answer == 'no':
                self.Exit_2048()
        if 2048 in chain(*game_grid):
            answer = tkinter.messagebox.askquestion('You Win !', 'Do you play a new game ?')
            if answer == 'yes':
                self.generate_game_at_first(self.rows, self.cols)
                self.game_grid(self.rows, self.cols)
            elif answer == 'no':
                self.Exit_2048()
        
    def check_end(self):
        '''
        This function is used to help to check the end of the game
        '''
        global game_grid
        if 0 in chain(*game_grid):
            return False
        else:
            game_grid_end = game_grid.copy()
            game_grid_after_end = game_grid_end.copy()
            for row in range(self.rows):
                game_grid_after_end[row] = merge(game_grid_after_end[row], 'Left')
            if 0 in chain(*game_grid_after_end):
                return False
            
            game_grid_after_end = game_grid_end.copy()
            game_grid_after_end = list(map(list, zip(*game_grid_after_end)))
            for col in range(self.cols):
                game_grid_after_end[col] = merge(game_grid_after_end[col], 'Up')
            game_grid_after_end = list(map(list, zip(*game_grid_after_end)))
            if 0 in chain(*game_grid_after_end):
                   return False
                
            game_grid_after_end = game_grid_end.copy()
            for row in range(self.rows):
                game_grid_after_end[row] = merge(game_grid_after_end[row], 'Right')
            if 0 in chain(*game_grid_after_end):
                   return False
                
            game_grid_after_end = game_grid_end.copy()    
            game_grid_after_end = list(map(list, zip(*game_grid_after_end)))
            for col in range(self.cols):
                game_grid_after_end[col] = merge(game_grid_after_end[col], 'Down')
            game_grid_after_end = list(map(list, zip(*game_grid_after_end)))
            if 0 in chain(*game_grid_after_end):
                   return False
        return True

    def Menu(self):
        '''
        This function is used to help to creat a menu of 2048 game
        '''
        menu = tk.Menu(self.GUI)
        self.GUI.config(menu=menu)
        subMenu = tk.Menu(menu)
        menu.add_cascade(label = 'File', menu = subMenu)
        subMenu.add_command(label="New Game", command = self.new_game)
        subMenu.add_separator()
        subMenu.add_command(label="Exit", command = self.Exit_2048)
        editMenu = tk.Menu(menu)
        menu.add_cascade(label = 'Edit', menu = editMenu)
        editMenu.add_command(label="Resize", command = self.Resize)

    def new_game(self):
        '''
        This function is used to help to creat new 2048 game
        '''
        self.Exit_2048()
        self.__init__(self.rows, self.cols)

    def Exit_2048(self):
        '''
        This function is used to help to exit 2048 game
        '''
        self.GUI.destroy()

    def Resize(self):
        '''
        This function is used to help to creat a new size of 2048 game
        '''
        self.resize = tk.Tk()
        self.resize.geometry('230x70')
        self.resize.title('Grid Size')
        self.label_1 = tk.Label(self.resize, text = "Rows (3-9)")
        self.label_2 = tk.Label(self.resize, text = "Columns (3-9)")
        self.label_3 = tk.Label(self.resize, text = "Press enter after chosing your grid size")
        self.entry_1 = tk.Entry(self.resize)
        self.entry_2 = tk.Entry(self.resize)
        self.label_1.grid(row='0', sticky = 'E')
        self.label_2.grid(row='1', sticky = 'E')
        self.entry_1.grid(row='0', column = '1')
        self.entry_2.grid(row='1', column = '1')
        self.label_3.grid(columnspan = '3', sticky = 'W')
        self.resize.bind("<Key>", self.Key)

    def Key(self, event1):
        '''
        This function is used to help to get a new size of 2048 game
        '''
        if str(event1.keysym) == 'Return' and int(self.entry_1.get()) >= 3 and int(self.entry_2.get()) >= 3 and int(self.entry_1.get()) < 10 and int(self.entry_2.get()) < 10:
            self.rows = int(self.entry_1.get())
            self.cols = int(self.entry_2.get())
            self.Exit_Resize()
            self.new_game()
        elif str(event1.keysym) == 'Return' and int(self.entry_1.get()) < 3:
            tkinter.messagebox.showinfo('Warning', 'Rows must be more than 3')
        elif str(event1.keysym) == 'Return' and int(self.entry_2.get()) < 3:
            tkinter.messagebox.showinfo('Warning', 'Columns must be more than 3')
        elif str(event1.keysym) == 'Return' and int(self.entry_1.get()) > 9:
            tkinter.messagebox.showinfo('Warning', 'Rows must be less than 10')
        elif str(event1.keysym) == 'Return' and int(self.entry_2.get()) > 9:
            tkinter.messagebox.showinfo('Warning', 'Columns must be less than 10')
        
    def Exit_Resize(self):
        '''
        This function is used to help to close Grid Size sindow
        '''
        self.resize.destroy()
#####################################################################################################################################
if __name__ == '__main__':
    Full_2048(4,4)
