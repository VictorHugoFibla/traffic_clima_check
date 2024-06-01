import unittest
from unittest.mock import MagicMock
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data import transformation
import datetime

class TestTransformation(unittest.TestCase):

    def test_clean_weather_data(self):
        # Dados de exemplo para limpeza
        data = {
            'name': 'Test City',
            'main': {'temp': 300, 'humidity': 50, 'pressure': 1013},
            'weather': [{'description': 'Clear'}],
            'dt': 1623432000
        }
        # Chamando a função de limpeza
        cleaned_data = transformation.clean_weather_data(data)
        # Verificando se os dados foram limpos corretamente
        self.assertEqual(len(cleaned_data), 1)
        self.assertEqual(cleaned_data[0]['city'], 'Test City')
        self.assertEqual(cleaned_data[0]['temperature'], 26.85)
        self.assertEqual(cleaned_data[0]['humidity'], 50)
        self.assertEqual(cleaned_data[0]['pressure'], 1013)
        self.assertEqual(cleaned_data[0]['weather_description'], 'Clear')
        self.assertIsInstance(cleaned_data[0]['datetime'], datetime.datetime)

    def test_clean_traffic_data(self):
        # Dados de exemplo para limpeza
        data = {
            'status': 'OK',
            'routes': [{
                'summary': 'Route summary',
                'legs': [{
                    'distance': {'text': '10 km'},
                    'duration': {'text': '30 mins'},
                    'start_address': 'Start address',
                    'end_address': 'End address',
                    'start_location': {'lat': 0, 'lng': 0},
                    'end_location': {'lat': 1, 'lng': 1},
                    'steps': [{'html_instructions': 'Step 1'}, {'html_instructions': 'Step 2'}]
                }]
            }]
        }
        # Chamando a função de limpeza
        cleaned_routes = transformation.clean_traffic_data(data)
        # Verificando se os dados foram limpos corretamente
        self.assertEqual(len(cleaned_routes), 1)
        self.assertEqual(cleaned_routes[0]['summary'], 'Route summary')
        self.assertEqual(cleaned_routes[0]['distance'], '10 km')
        self.assertEqual(cleaned_routes[0]['duration'], '30 mins')
        self.assertEqual(cleaned_routes[0]['start_address'], 'Start address')
        self.assertEqual(cleaned_routes[0]['end_address'], 'End address')
        self.assertEqual(cleaned_routes[0]['start_location'], {'lat': 0, 'lng': 0})
        self.assertEqual(cleaned_routes[0]['end_location'], {'lat': 1, 'lng': 1})
        self.assertEqual(cleaned_routes[0]['steps'], ['Step 1', 'Step 2'])

if __name__ == '__main__':
    unittest.main()
