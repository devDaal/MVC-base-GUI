from tkinter import Frame, PhotoImage, Label, Button

logo_photo_path = "C:/Users/ITS_Servicio/Desktop/Desarrollo Software Diego/Learning/Intento de MVC B3C/app/images/new_logo.png"  # line 23
send_home_photo_path = "C:/Users/ITS_Servicio/Desktop/Desarrollo Software Diego/Learning/Intento de MVC B3C/app/images/home.png"  # line 3

class LeftHomePage(Frame):
    
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        
        self.place_logo()
        self.place_send_home_btn()
        self.place_exit_btn()
        
        self.config(bg="#7f7f7f")
        
    def place_logo(self):
        self.logo_photo = PhotoImage(file= logo_photo_path).subsample(2,2)
        self.logo= Label(self,bg="gray",image = self.logo_photo)
        self.logo.grid(row=0,column=1)
    
    def place_send_home_btn(self):
        container = Frame(self, bg= "#7f7f7f")
        container.grid(row=1, column=0, pady=(10,0), padx=(10,0))
        self.send_home_photo = PhotoImage(file= send_home_photo_path).subsample(8,8)
        self.send_home_btn = Button(container, image=self.send_home_photo)#Podría poner una casita de logo con una flecha
        self.send_home_btn.grid()
        self.send_home_lbl = Label(container, text="Home", bg= "#7f7f7f")
        self.send_home_lbl.grid(row=1)
    
    def place_exit_btn(self):
        self.exit_btn = Button(self, text="EXIT", font=('Robot', 12, 'bold'), bg="red", fg="white")
        self.exit_btn.grid(row=3, column=1)
        