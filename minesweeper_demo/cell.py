from tkinter import Button
class Cell:
    
    def __init__(self, is_mine=False) -> None:
        self.is_mine=False
        self.cell_btn_object = None

    def create_btn_object(self, location):
        btn = Button(
            location,
            text='Text'
        )
        self.cell_btn_object = btn