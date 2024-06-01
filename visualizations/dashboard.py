import os
import sys
import json
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

def get_weather_data_from_db():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM weather ORDER BY datetime DESC")
    weather_data = cur.fetchall()
    conn.close()

    weather_data_dicts = []
    for row in weather_data:
        weather_data_dicts.append({
            'id': row[0],
            'city': row[1],
            'temperature': row[2],
            'humidity': row[3],
            'pressure': row[4],
            'weather_description': row[5],
            'datetime': row[6]
        })
    return weather_data_dicts

def get_traffic_data_from_db():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM traffic ORDER BY id DESC")
    traffic_data = cur.fetchall()
    conn.close()

    traffic_data_dicts = []
    for row in traffic_data:
        traffic_data_dicts.append({
            'id': row[0],
            'summary': row[1],
            'distance': row[2],
            'duration': row[3],
            'start_address': row[4],
            'end_address': row[5],
            'start_location': json.loads(row[6]),
            'end_location': json.loads(row[7]),
            'steps': json.loads(row[8])
        })
    return traffic_data_dicts


def create_dash_app(weather_data, traffic_data):
    app = dash.Dash(__name__)
    app.title = "Dashboard de Clima e Tráfego"

    # Ajustar o índice das colunas de acordo com a tabela `weather`
    weather_x = [row[6] for row in weather_data]
    weather_y = [row[2] for row in weather_data]

    # Criar o texto do ponto com a cidade
    weather_text = [f"{row[1]} ({row[6]})" for row in weather_data]

    # Ajustar o índice das colunas de acordo com a tabela `traffic`
    traffic_x = [f"{row[4]} -> {row[5]}" for row in traffic_data]
    traffic_y = []
    for route in traffic_data:
        duration_parts = route[3].split()
        minutes = 0
        for i in range(0, len(duration_parts), 2):
            if duration_parts[i + 1].startswith('hour'):
                minutes += int(duration_parts[i]) * 60
            elif duration_parts[i + 1].startswith('min'):
                minutes += int(duration_parts[i])
        traffic_y.append(minutes)

    app.layout = html.Div(style={'backgroundColor': '#f9f9f9', 'font-family': 'Arial, sans-serif'}, children=[
        html.H1('Dashboard de Clima e Tráfego', style={'textAlign': 'center', 'padding': '20px', 'color': '#333'}),

        html.Div([
            dcc.Graph(
                id='weather-graph',
                figure={
                    'data': [{
                        'x': weather_x,
                        'y': weather_y,
                        'type': 'scatter',
                        'mode': 'lines+markers',
                        'name': 'Temperatura (°C)',
                        'text': weather_text,  # Adiciona o texto do ponto com a cidade
                        'line': {'color': 'blue'}
                    }],
                    'layout': {
                        'title': 'Temperatura ao longo do tempo',
                        'xaxis': {'title': 'Data/Hora'},
                        'yaxis': {'title': 'Temperatura (°C)'},
                        'plot_bgcolor': '#fff',
                        'paper_bgcolor': '#f9f9f9'
                    }
                }
            )
        ], style={'padding': '20px'}),

        html.Div([
            dcc.Graph(
                id='traffic-graph',
                figure={
                    'data': [{
                        'x': traffic_x,
                        'y': traffic_y,
                        'type': 'scatter',
                        'mode': 'markers',
                        'name': 'Duração da Viagem (minutos)',
                        'marker': {'color': 'red'}
                    }],
                    'layout': {
                        'title': 'Duração da Viagem de Diferentes Rotas',
                        'xaxis': {'title': 'Rotas'},
                        'yaxis': {'title': 'Duração (minutos)'},
                        'plot_bgcolor': '#fff',
                        'paper_bgcolor': '#f9f9f9'
                    }
                }
            )
        ], style={'padding': '20px'})
    ])

    return app


