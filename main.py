from tkinter import *
from cell import Cell
import settings
import utils

root = Tk() #a window
#windows settings
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')   #set size of window
root.title("MineSweeper Game")
root.resizable(False, False)    #dont let window be resizable.

#Change use for some info
top_frame = Frame(
    root, 
    bg='black',
    width=settings.WIDTH,
    height=utils.height_percent(25)
)
top_frame.place(x=0,y=0)

left_frame=Frame(
    root, 
    bg='black',
    width=utils.width_percent(25),
    height=utils.height_percent(75)
)
left_frame.place(x=0,y=utils.height_percent(25))

#Main Game section of window
center_frame = Frame(
    root, 
    bg='red',
    width=utils.width_percent(75),
    height=utils.height_percent(75)
)

center_frame.place(
    x=utils.width_percent(25),
    y=utils.height_percent(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c=Cell(x,y)
        c.create_btn_obj(center_frame)
        c.cell_button_obj.grid(column=x, row=y)

# print(Cell.all)
Cell.randomize_mines()

#Run window
root.mainloop()