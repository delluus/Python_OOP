from tkinter import *
from cell import Cell
import settings


root = Tk()
# Override the settings of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg="black",
    width=settings.WIDTH,
    height=settings.HEIGHT/4
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH/4,
    height=settings.HEIGHT*3/4
)
left_frame.place(x=0, y=settings.HEIGHT/4)

centre_frame = Frame(
    root,
    bg="black",
    width=settings.WIDTH*3/4,
    height=settings.HEIGHT
)
centre_frame.place(x=settings.WIDTH/4, y=settings.HEIGHT/4)

# Setup grid ##
for y in range(settings.GRID_SIZE):
    for x in range(settings.GRID_SIZE):
        c = Cell()
        c.create_btn_object(centre_frame)
        c.cell_btn_object.grid(
            column=y,
            row   =x
        )


# Run the window
root.mainloop()

