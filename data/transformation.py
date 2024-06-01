import datetime

def clean_weather_data(data):
    cleaned_data = [{
        'city': data.get('name'),
        'temperature': round(data['main'].get('temp') - 273.15, 2),  # Convertendo de Kelvin para Celsius
        'humidity': data['main'].get('humidity'),
        'pressure': data['main'].get('pressure'),
        'weather_description': data['weather'][0].get('description'),
        'datetime': datetime.datetime.fromtimestamp(data.get('dt'))
    }]
    return cleaned_data

def clean_traffic_data(data):
    cleaned_routes = []
    if data.get('status') == 'OK':
        routes = data.get('routes', [])
        for route in routes:
            cleaned_routes.append({
                'summary': route.get('summary'),
                'distance': route['legs'][0]['distance'].get('text'),
                'duration': route['legs'][0]['duration'].get('text'),
                'start_address': route['legs'][0].get('start_address'),
                'end_address': route['legs'][0].get('end_address'),
                'start_location': route['legs'][0]['start_location'],
                'end_location': route['legs'][0]['end_location'],
                'steps': [step['html_instructions'] for step in route['legs'][0]['steps']]
            })
    return cleaned_routes
