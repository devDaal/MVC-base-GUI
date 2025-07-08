from views.main import View
from models.main import Model

class LeftPageController:
    
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        self.frame = self.view.frames["left_page"]
        self._bind()
        
    def _bind(self):
        self.frame.exit_btn.config(command = self.home_page) 
        self.frame.send_home_btn.config(command = self.window1_page)
    def home_page(self):
        self.view.switch("startpage")
        
    def window1_page(self):
        print("window1")
        self.view.switch("window1_page")
    
    def say_hello(self):
        self.model.hello.say_hello()