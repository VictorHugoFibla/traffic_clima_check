import os
import sys

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.loading import get_db_connection, select_weather_data, select_traffic_data
from visualizations.dashboard import create_dash_app

def run_app():
    # Conexão com o banco de dados
    conn = get_db_connection()
    
    # Seleciona os dados de clima e tráfego do banco de dados
    weather_data = select_weather_data(conn)
    traffic_data = select_traffic_data(conn)
    
    # Fecha a conexão com o banco de dados
    conn.close()

    # Criação do app Dash
    app = create_dash_app(weather_data, traffic_data)
    app.run_server(debug=True)

if __name__ == '__main__':
    run_app()
