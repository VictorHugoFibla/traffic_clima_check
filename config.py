import os
# Configurações da API
OPENWEATHER_API_KEY = os.getenv('SuaApiKeyDoOpenWeather')

# Se você ainda não tem uma chave da API do Google, siga estas etapas para obtê-la:
# 1. Acesse o Google Cloud Console: https://console.cloud.google.com/
# 2. Faça login ou crie uma conta.
# 3. Selecione um projeto existente ou crie um novo.
# 4. No painel de navegação, clique em "Credenciais".
# 5. Crie uma nova chave da API e cole-a abaixo.

GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY', 'SuaChaveDaAPIdoGoogle')

# Configurações do banco de dados
DB_NAME = 'Zebrinha Azul'  # Alterado para o nome do banco de dados
DB_USER = 'postgres'
DB_PASSWORD = 'teste'
DB_HOST = 'localhost'
DB_PORT = '5432'
