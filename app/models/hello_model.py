from app.models.base import ObservableModel
import requests

class Hello_Test(ObservableModel):
    
    def __init__(self):
        super().__init__()
        """self.counter += 1
        print("Hello Test", self.counter)"""
        self.hello_counter = 0
        
    def say_hello(self) -> None:
        self.hello_counter += 1
        self.trigger_event("Hello")
        
    def get_joke(self):
        url = "https://official-joke-api.appspot.com/random_joke"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    joke = response.json()['setup']
                except Exception:
                    joke = 'No jokes (invalid JSON)'
            else:
                joke = 'No jokes (bad status)'
        except Exception:
            joke = 'No jokes (connection error)'
            
        #self.trigger_event("joke", joke)
        return joke