from tkinter import Tk

class Root(Tk):
    
    def __init__(self):
        Tk.__init__(self)
           
        start_width = 550
        min_width = 400
        start_height = 380
        min_height = 250
        
        self.geometry(f"{start_width}x{start_height}")
        self.minsize(width=min_width, height=min_height)
        self.title("Test with B3C")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)