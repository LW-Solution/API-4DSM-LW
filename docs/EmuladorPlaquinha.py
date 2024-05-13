import requests
import random
from datetime import datetime, timedelta

# Conexão com o banco de dados
url = "http://host.docker.internal:3001/measure"  # Alterado para HTTP

# Defina a data de início e fim para o mês de abril de 2024
start_date = datetime(2024, 5, 1, 0, 0, 0)  # Início à meia-noite
end_date = datetime(2024, 5, 8)  # Fim no último dia do mês

# Loop para inserir registros
i = 1
current_date = start_date
while current_date < end_date and current_date.hour < 24:  # Verifica se a hora atual é menor que 24
    unixtime = int(current_date.timestamp())
    for j in [1, 2, 3]:  # Loop para cada parâmetro
        id_measure = (i - 1) * 6 + j  # Cálculo para gerar IDs únicos para cada registro
        value = random.randint(5, 40)  # Valores aleatórios entre 10 e 40
        stationParameterStationParameterId = j
        
        data = {
            "value": value,
            "unixtime": unixtime,
            "station_parameter_id": {
            "station_parameter_id": stationParameterStationParameterId
            }
        }
        print(data)
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print(f"Registro {i} inserido com sucesso!")
        else:
            print(f"Erro ao inserir o registro {i}. Código de status: {response.status_code}")
            print(response.text)
    
    i += 1
    current_date += timedelta(hours=1)  # Avança uma hora