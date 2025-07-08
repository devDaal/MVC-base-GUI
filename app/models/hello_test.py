from .base import ObservableModel

class Hello_Test(ObservableModel):
    
    def __init__(self):
        super().__init__()
        """self.counter += 1
        print("Hello Test", self.counter)"""
        self.hello_counter = 0
        
    def say_hello(self) -> None:
        self.hello_counter += 1
        self.trigger_event("Hello")