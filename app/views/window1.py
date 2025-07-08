from tkinter import Frame, Label, Button

class Window1(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.place_title()
        self.place_exit_btn()
        
    def place_title(self):
        title = Label(self, text="Window 1",font=("Robot",12,"normal"))
        title.grid()
        
    def place_exit_btn(self):
        self.exit_btn = Button(self, text='EXIT',
                               font=("Robot",12,"bold"), bg='red', fg='white')
        self.exit_btn.grid(row=5)
        