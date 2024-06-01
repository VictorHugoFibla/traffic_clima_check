import unittest
from unittest.mock import patch
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data import extraction  # Corrigindo o import do módulo de extração

class TestExtraction(unittest.TestCase):

    @patch('data.extraction.requests.get')  # Corrigindo o caminho para o patch
    def test_get_weather_data(self, mock_get):
        # Mocking a response
        mock_get.return_value.json.return_value = {'name': 'Test City', 'main': {'temp': 300, 'humidity': 50, 'pressure': 1013}, 'weather': [{'description': 'Clear'}], 'dt': 1623432000}
        
        city = 'Test City'
        weather_data = extraction.get_weather_data(city)
        
        self.assertEqual(weather_data['city']['city'], 'Test City')
        self.assertEqual(weather_data['temperature']['temperature'], 26.85)
        self.assertEqual(weather_data[0]['humidity'], 50)
        self.assertEqual(weather_data[0]['pressure'], 1013)
        self.assertEqual(weather_data[0]['weather_description'], 'Clear')

    @patch('data.extraction.requests.get')  # Corrigindo o caminho para o patch
    def test_get_traffic_data(self, mock_get):
        # Mocking a response
        mock_get.return_value.json.return_value = {'status': 'OK', 'routes': [{'summary': 'Route summary', 'legs': [{'distance': {'text': '10 km'}, 'duration': {'text': '30 mins'}, 'start_address': 'Start address', 'end_address': 'End address', 'start_location': {'lat': 0, 'lng': 0}, 'end_location': {'lat': 1, 'lng': 1}, 'steps': [{'html_instructions': 'Step 1'}, {'html_instructions': 'Step 2'}]}]}]}
        
        origin = 'Origin'
        destination = 'Destination'
        traffic_data = extraction.get_traffic_data(origin, destination)
        
        self.assertEqual(traffic_data[0]['summary'], 'Route summary')
        self.assertEqual(traffic_data[0]['distance'], '10 km')
        self.assertEqual(traffic_data[0]['duration'], '30 mins')
        self.assertEqual(traffic_data[0]['start_address'], 'Start address')
        self.assertEqual(traffic_data[0]['end_address'], 'End address')
        self.assertEqual(traffic_data[0]['start_location'], {'lat': 0, 'lng': 0})
        self.assertEqual(traffic_data[0]['end_location'], {'lat': 1, 'lng': 1})
        self.assertEqual(traffic_data[0]['steps'], ['Step 1', 'Step 2'])

if __name__ == '__main__':
    unittest.main()
