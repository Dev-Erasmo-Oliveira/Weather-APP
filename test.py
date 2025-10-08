import requests
import datetime
import json

chave_api = '3c1c80103ca742ce9a7151348250610'
cidade = 'São Paulo'
api_link = f"http://api.weatherapi.com/v1/current.json?key={chave_api}&lang=pt&q={cidade}"

#-----fazendo a chamada da APi-----#
r = requests.get(api_link)

#-----convertendo os dados da variavel r em dicionario  (JSON) -----#
dados = r.json()

#-----Obtendo Pais, Zona e horário-----#
info_pais = (
    dados['location']['name'],
    dados['location']['region'],
    dados['location']['country'],
    dados['location']['tz_id'],
    dados['location']['localtime']
)
print(info_pais)

#------Tempo-----#
tempo = (
    dados['current']['temp_c'],
    dados['current']['condition']['text'],  # precisa acessar o texto dentro do dict 'condition'
    dados['current']['wind_kph'],
    dados['current']['pressure_mb'],
    dados['current']['humidity'],
    dados['current']['cloud'],
    dados['current']['feelslike_c']
)

