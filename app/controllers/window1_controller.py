from views.main import View
from models.main import Model

class Window1Controller:
    
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        self.frame = self.view.frames["window1_page"]
        self._bind()
        
    def _bind(self):
        self.frame.exit_btn.config(command = self.home_page)     
        
    def home_page(self):
        self.view.switch("left_page")
        #Se pueden hacer más acciones como deshabilitar el botón, pero creo que por ahora está bien
        #Se podría también mandar un mensaje de que no se puede salir porque la prueba está corriendo