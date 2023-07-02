from tkinter import Button
import random
import settings

class Cell:
    all = []

    #is_mine is a landmine.
    def __init__(self,x,y,is_mine=False):
        self.is_mine=is_mine
        self.cell_button_obj = None
        self.x=x
        self.y=y

        #Append the object to the Cell.all list
        Cell.all.append(self)


    def create_btn_obj(self, location):
        # self.randomize_mines()
        buttn = Button(
            location,
            # bg="green",
            width=8,
            height=4,
            text=f"{self.x},{self.y}"
        )

        buttn.bind('<Button-1>', self.left_click_actions)
        buttn.bind('<Button-3>', self.right_click_actions)

        self.cell_button_obj = buttn

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

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

    def show_cell(self):
        
        print(self.surrounded_cells)

    def show_mine(self):
        # interrrupt game and display message player lost
        self.cell_button_obj.configure(bg="red")

    def right_click_actions(self, event):
        print(event)
        print("right click")


    @staticmethod
    #Make random landmines for the game
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"