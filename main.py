from data.extraction import get_weather_data, get_traffic_data
from data.transformation import clean_weather_data, clean_traffic_data
from data.loading import get_db_connection, insert_weather_data, insert_traffic_data
import re  # Módulo para manipulação de expressões regulares

def is_valid_input(input_string):
    # Verifica se a entrada contém apenas letras e espaços
    if not re.match("^[a-zA-Z\s]+$", input_string):
        return False
    return True

def main():
    # Extração de dados
    city_verify_weather = input("Digite a cidade que deseja extrair o clima sem acento ou caracteres especiais: ")
    while not is_valid_input(city_verify_weather):
        print("Erro: A cidade deve conter apenas letras e espaços.")
        city_verify_weather = input("Digite novamente a cidade: ")

    city_start = input("Digite a cidade inicial: ")
    while not is_valid_input(city_start):
        print("Erro: A cidade inicial deve conter apenas letras e espaços.")
        city_start = input("Digite novamente a cidade inicial: ")

    city_end = input("Digite a cidade final: ")
    while not is_valid_input(city_end):
        print("Erro: A cidade final deve conter apenas letras e espaços.")
        city_end = input("Digite novamente a cidade final: ")

    # Obtém os dados climáticos e de tráfego
    weather_data = get_weather_data(city_verify_weather)
    traffic_data = get_traffic_data(city_start, city_end)

    # Limpeza e transformação dos dados
    cleaned_weather_data = clean_weather_data(weather_data)
    cleaned_traffic_data = clean_traffic_data(traffic_data)

    # Carregamento dos dados no banco de dados
    conn = get_db_connection()
    insert_weather_data(conn, cleaned_weather_data)
    insert_traffic_data(conn, cleaned_traffic_data)
    conn.close()

if __name__ == '__main__':
    main()
