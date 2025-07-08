from tkinter import Button, Frame, Label, StringVar, Radiobutton
from tkinter.ttk import Combobox

class Settingsview(Frame):
    
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        
        self.place_title()
        self.place_exit_btn()
        self.place_test_widget()
        self.place_port_selection_widget()
        
        self.grid_rowconfigure(3,minsize=80) #This is here to keep the exit button on its place
        
        
    def place_exit_btn(self):
        self.exit_btn = Button(self, text="EXIT", 
                               font=("Robot",12,"bold"), bg='red', fg='white')
        self.exit_btn.grid(row=3, sticky='sw', padx=5) 
        
    def place_title(self):
        title = Label(self, text='SETTINGS', font = ("Robot",12,"bold"))
        title.grid(row=0,column=0,padx=10, pady=10)
        
    def place_port_selection_widget(self):
        
        self.selected_connection_method = StringVar()
        self.selected_connection_method.set("0") #This is just here for the radios to start unselected
        self.radio_COM = Radiobutton(self, text='SERIAL PORTS',font=("Robot",12,"normal"),
                                    value='port', variable=self.selected_connection_method)
        self.radio_COM.grid(column=1, row=0, sticky='w')
        
        self.serial_port_container = Frame(self)
        self.serial_port_container.grid(column=1, row=1)
        
        self.combo_port = Combobox(self.serial_port_container, state='readonly')
        self.combo_port.grid(row=0)       
        
        self.update_ports_btn = Button(self.serial_port_container, text="UPDATE",
                                  font=("Robot",8,"bold"),fg='white',bg='blue')    
        self.update_ports_btn.grid(row=0,column=1, padx=5)
        
        self.connect_btn = Button(self.serial_port_container, text="CONNECT", width=11,
                                  font=("Robot",12,"bold"),fg='white',bg='green')    
        self.connect_btn.grid(row=2,column=1, padx=5, pady=(5,0))
        
    def place_test_widget(self):
        self.tcp_test_btn = Button(self, text="TEST", width=11,
                                  font=("Robot",12,"bold"),fg='white',bg='green')    
        self.tcp_test_btn.grid(row=2,column=2, padx=5, pady=(5,0))
        
