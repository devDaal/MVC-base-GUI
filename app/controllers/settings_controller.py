from app.views.main import View
from app.models.main import Model

class SettingsController:
    
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        self.frame = self.view.frames["settings_page"]
        self._bind()
        
    def _bind(self):
        self.frame.exit_btn.config(command = self.start_page)
        self.frame.tcp_test_btn.config(command = self.test)
        
    def test(self):
        print("Testito")
        joke = self.model.hello.get_joke()
        print("The joke is", joke['setup'])
        return len(joke['setup'])
        
    
    def start_page(self):
        self.view.switch("startpage")