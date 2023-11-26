import requests
from config import CHAVE_API_OPENWEATHERMAP

def obter_dados_meteorologicos(cidade, chave_api):
    # URL da API do OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}"

    # Fazendo a requisição à API
    resposta = requests.get(url)

    # Verificando se a requisição foi bem-sucedida (código 200)
    if resposta.status_code == 200:
        # Convertendo os dados JSON em um dicionário Python
        dados = resposta.json()

        # Extraindo informações relevantes
        temperatura = dados['main']['temp']
        sensacao_termica = dados['main']['feels_like']

        return temperatura, sensacao_termica
    else:
        # Em caso de erro na requisição, imprima o código de status
        print(f"Erro na requisição: {resposta.status_code}")
        return None, None

if __name__ == "__main__":
    # Lembre de colocar sua chave API aqui (Para criar: https://openweathermap.org/api)
    # Cuidado para não expor no GitHub hahaha
    SUA_CHAVE_API = CHAVE_API_OPENWEATHERMAP
    temperatura, sensacao_termica = obter_dados_meteorologicos('Feira de Santana', SUA_CHAVE_API)
    if temperatura is not None and sensacao_termica is not None:
        temp_data = f"Temperatura em Feira de Santana: {temperatura}°C\n" + f"Sensação térmica: {sensacao_termica}°C"
    else:
        temp_data = "Não foi possível obter os dados meteorológicos."
    print(temp_data)

