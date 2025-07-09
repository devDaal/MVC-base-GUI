"""This module is for the first tests I have ever done
"""
from unittest.mock import patch, MagicMock
import unittest
from app.models.main import Model
from app.views.main import View
from app.controllers.settings_controller import SettingsController



class TestJoke(unittest.TestCase):
    
    @patch('app.models.hello_model.Hello_Test.get_joke')
    def test_len_joke(self, mock_get_joke):
        model = Model()
        view = View()
        self.controller = SettingsController(model, view)
        mock_get_joke.return_value = {'setup':'four'}
        self.assertEqual(self.controller.test(), 4)        
    
    @patch('app.models.hello_model.requests')
    def test_get_joke(self, mock_requests):
        
        model = Model()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = { 'id': 1,
                                            'type': 'general',
                                            'setup': 'four',
                                            'punchline': 'test punchline'}
        print(mock_response, "mock response")
        
        mock_requests.get.return_value = mock_response
        
        self.assertEqual(model.hello.get_joke(), 'four')
    
    @patch('app.models.hello_model.requests')    
    def test_fail_get_joke(self, mock_requests):
        
        model = Model()
        mock_response = MagicMock(status_code = 403)
        mock_response.json.return_value = { 'id': 1,
                                            'type': 'general',
                                            'setup': 'four',
                                            'punchline': 'test punchline'}
        print(mock_response, "mock response")
        
        mock_requests.get.return_value = mock_response
        
        self.assertEqual(model.hello.get_joke(), 'No jokes (bad status)')

if __name__ == '__main__':
    unittest.main()
