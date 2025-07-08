from tkinter import Button, Frame, Label

class Settingsview(Frame):
    
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        
        self.place_title()
        self.place_exit_btn()
        self.place_test_widget()
        
        self.grid_rowconfigure(3,minsize=80) #This is here to keep the exit button on its place
        
        
    def place_exit_btn(self):
        self.exit_btn = Button(self, text="EXIT", 
                               font=("Robot",12,"bold"), bg='red', fg='white')
        self.exit_btn.grid(row=3, sticky='sw', padx=5) 
        
    def place_title(self):
        title = Label(self, text='SETTINGS', font = ("Robot",12,"bold"))
        title.grid(row=0,column=0,padx=10, pady=10)
        
    def place_test_widget(self):
        self.tcp_test_btn = Button(self, text="TEST", width=11,
                                  font=("Robot",12,"bold"),fg='white',bg='green')    
        self.tcp_test_btn.grid(row=2,column=2, padx=5, pady=(5,0))
        
