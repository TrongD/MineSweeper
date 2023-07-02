from tkinter import Button, Label, messagebox
import random
import settings
import ctypes

class Cell:
    all = []
    cell_count=settings.CELL_COUNT
    cell_count_label_object = None

    def __init__(self,x,y,is_landmine=False):
        self.is_landmine=is_landmine
        self.is_opened=False
        self.is_mine_candidate=False
        self.cell_button_obj = None
        self.x=x
        self.y=y

        #Append the object to the Cell.all list
        Cell.all.append(self)


    def create_btn_obj(self, location):
        # self.randomize_mines()
        buttn = Button(
            location, 
            # activebackground="gray85",
            width=8,
            height=4,
            # text=f"{self.x},{self.y}"
        )

        buttn.bind('<Button-1>', self.left_click_actions)
        buttn.bind('<Button-3>', self.right_click_actions)
        self.cell_button_obj = buttn

    @staticmethod
    def create_cell_count_label(location):
        lbl =Label(
            location,
            bg="green",
            fg="white",
            text= f"Cells Left: {Cell.cell_count}",
            width=12,
            height=4,
            font=("",20)
        )
        Cell.cell_count_label_object = lbl

    def left_click_actions(self, event):
        if self.is_landmine:
            self.show_landmine()
        else:
            if self.surrounded_cells_mines_length ==0:
                for cell in self.surrounded_cells:
                    
                    cell.show_cell()
                    # self.cell_button_obj.configure(bg="green")
                    
            
            self.show_cell()
            # self.cell_button_obj.configure(bg="white")

    #return a cell object based on x,y location
    def get_cell_by_axis(self, x,y):
        for cell in Cell.all:
            if cell.x ==x and cell.y ==y:
                return cell
    @property
    def surrounded_cells(self):
        cells=[
            self.get_cell_by_axis(self.x-1, self.y-1),
            self.get_cell_by_axis(self.x-1, self.y),
            self.get_cell_by_axis(self.x-1, self.y+1),
            self.get_cell_by_axis(self.x, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y),
            self.get_cell_by_axis(self.x+1, self.y+1),
            self.get_cell_by_axis(self.x, self.y+1)
        ]
        
        cells = [cell for cell in cells if cell is not None]
        return cells

    #check adjacent cell if its a landmine.
    @property
    def surrounded_cells_mines_length(self):
        counter =0
        for cell in self.surrounded_cells:
            if cell.is_landmine:
                counter+=1

        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_button_obj.configure(bg="green",text=self.surrounded_cells_mines_length)
            # self.cell_button_obj.configure(bg="green")
            #replace text of cell count with newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left: {Cell.cell_count}"
                )

        #mark cell as opened
        self.is_opened=True

    def show_landmine(self):
        
        self.cell_button_obj.configure(bg="red")
        # ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over', 0)
        # tkinter.messagebox.showinfo(title=Hi, message=Bye, **options)
        # mssg=message("d")
        # mssg.showinfo(title=Hi, message=Bye, **options)

        # ttk.Button(
        #     root,
        #     text='Show an warning message',
        #     command=lambda: showwarning(
        #         title='Warning',
        #         message='This is a warning message.')
        # ).pack(**options)
        # tkinter.messagebox.showinfo("Welcome to GFG", "South Button clicked")


    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_button_obj.configure(
                bg="orange"
            )
            self.is_mine_candidate=True
        else:
            self.cell_button_obj.configure(
                 bg='gray85'               
            )
            self.is_mine_candidate=False


    @staticmethod
    #Make random landmines for the game
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_landmine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"