import requests

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

        return temperatura, sensacao_termica, resposta.status_code

    # Em caso de erro na requisição, imprima o código de status
    return None, None, resposta.status_code
