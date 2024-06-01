import unittest
from unittest.mock import MagicMock
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data import loading

class TestLoading(unittest.TestCase):

    def setUp(self):
        # Configurando um mock para a conexão com o banco de dados
        self.mock_conn = MagicMock()

    def test_get_db_connection(self):
        # Testando a função get_db_connection
        connection = loading.get_db_connection()
        # Verificando se a conexão foi criada corretamente
        self.assertIsNotNone(connection)

    def test_insert_weather_data(self):
        # Dados de exemplo para inserção
        data = [{
            'city': 'Test City',
            'temperature': 25,
            'humidity': 50,
            'pressure': 1013,
            'weather_description': 'Clear',
            'datetime': '2024-06-01 12:00:00'
        }]
        # Chamando a função de inserção com o mock da conexão
        loading.insert_weather_data(self.mock_conn, data)
        # Verificando se a função interagiu corretamente com o cursor
        self.mock_conn.cursor.return_value.__enter__.return_value.execute.assert_called_once()

    def test_insert_traffic_data(self):
        # Dados de exemplo para inserção
        data = [{
            'summary': 'Test Route',
            'distance': '10 km',
            'duration': '30 mins',
            'start_address': 'Start address',
            'end_address': 'End address',
            'start_location': {'lat': 0, 'lng': 0},
            'end_location': {'lat': 1, 'lng': 1},
            'steps': ['Step 1', 'Step 2']
        }]
        # Chamando a função de inserção com o mock da conexão
        loading.insert_traffic_data(self.mock_conn, data)
        # Verificando se a função interagiu corretamente com o cursor
        self.mock_conn.cursor.return_value.__enter__.return_value.execute.assert_called_once()

    def test_select_weather_data(self):
        # Configurando o retorno esperado da consulta
        expected_data = [('Test City', 25, 50, 1013, 'Clear', '2024-06-01 12:00:00')]
        self.mock_conn.cursor.return_value.__enter__.return_value.fetchall.return_value = expected_data
        # Chamando a função de seleção com o mock da conexão
        weather_data = loading.select_weather_data(self.mock_conn)
        # Verificando se a função interagiu corretamente com o cursor
        self.mock_conn.cursor.return_value.__enter__.return_value.execute.assert_called_once()
        # Verificando se os dados retornados são os esperados
        self.assertEqual(weather_data, expected_data)

    def test_select_traffic_data(self):
        # Configurando o retorno esperado da consulta
        expected_data = [('Test Route', '10 km', '30 mins', 'Start address', 'End address', '{"lat": 0, "lng": 0}', '{"lat": 1, "lng": 1}', '["Step 1", "Step 2"]')]
        self.mock_conn.cursor.return_value.__enter__.return_value.fetchall.return_value = expected_data
        # Chamando a função de seleção com o mock da conexão
        traffic_data = loading.select_traffic_data(self.mock_conn)
        # Verificando se a função interagiu corretamente com o cursor
        self.mock_conn.cursor.return_value.__enter__.return_value.execute.assert_called_once()
        # Verificando se os dados retornados são os esperados
        self.assertEqual(traffic_data, expected_data)

if __name__ == '__main__':
    unittest.main()
