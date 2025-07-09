from views.main import View
from models.main import Model

from .startpage import StartPageController
from .left_page_controller import LeftPageController
from .settings_controller import SettingsController
from .window1_controller import Window1Controller

class Controller:
    
    def __init__(self, model: Model, view: View) -> None:
        self.view = view
        self.model = model
        self.start_page_controller = StartPageController(model, view)
        self.with_B3C_page_controller = LeftPageController(model, view)
        self.settings_page_controller = SettingsController(model, view)
        self.homing_page_controller = Window1Controller(model, view)
        self.model.hello.add_event_listener("Hello", self.hello_world)
        self.model.hello.add_event_listener("joke", self.settings_page_controller.len_joke)
        
   #def event_to_update_view_using_variables_etc_from_model(self, parent):
       #update the view using methods and variables from the model through parent.bla bla bla

    def hello_world(self, parent):
        print(parent.hello_counter, "Hello World!")
        
    def start(self) -> None:
        self.view.start_mainloop()