from tkinter import Frame, Button, PhotoImage, Label

controller_photo_path = "C:/Users/ITS_Servicio/Desktop/Desarrollo Software Diego/Learning/Intento de MVC B3C/app/images/controller.png" #line 22
no_control_photo_path = "C:/Users/ITS_Servicio/Desktop/Desarrollo Software Diego/Learning/Intento de MVC B3C/app/images/no_control(3).png" #line 27
settings_photo_path = "C:/Users/ITS_Servicio/Desktop/Desarrollo Software Diego/Learning/Intento de MVC B3C/app/images/settings.png" #line 32
logo_photo_path = "C:/Users/ITS_Servicio/Desktop/Desarrollo Software Diego/Learning/Intento de MVC B3C/app/images/new_logo.png" #line 37

class StartPageview(Frame):
    
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        
        #self.config['bg'] = 'gray'
        
        self.config(bg= "#7f7f7f")
        self.place_left_button()
        self.place_right_button()
        self.place_settings_button()
        self.place_logo()
        
    def place_left_button(self):
        self.controller_photo = PhotoImage(file= controller_photo_path).subsample(12,12)
        self.left_btn = Button(self, image=self.controller_photo, width=62, height=62)
        self.left_btn.grid(row=2, column=0)
    
    def place_right_button(self):
        self.no_control_photo = PhotoImage(file= no_control_photo_path).subsample(16,16)
        self.right_btn = Button(self, image=self.no_control_photo)
        self.right_btn.grid(row=2, column=2)
    
    def place_settings_button(self):
        self.settings_photo = PhotoImage(file= settings_photo_path).subsample(12,12)
        self.settings_btn = Button(self, image=self.settings_photo, width=62, height=62)
        self.settings_btn.grid(row=2, column=1)
    
    def place_logo(self):
        self.logo_photo = PhotoImage(file= logo_photo_path).subsample(2,2)
        self.logo= Label(self,bg="gray",image = self.logo_photo)
        self.logo.grid(row=0,column=1, pady=(0,10))
    
        