from views.main import View
from models.main import Model

class StartPageController:
    
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        self.frame = self.view.frames["startpage"]
        self._bind()
        
    def _bind(self):
        self.frame.left_btn.config(command = self.left_page)        #Por qué no existe el hilo aquí? 
#        self.frame.right_btn.config(command = self.right_page)   por qué no se conecta con el botón en la vista?
        self.frame.settings_btn.config(command = self.settings_page)
        
    def left_page(self):
        self.view.switch("left_page")
    
    def right_page(self):
        self.view.switch("right_page")
        
    def settings_page(self):
        self.view.switch("settings_page")