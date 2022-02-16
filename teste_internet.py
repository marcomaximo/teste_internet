import speedtest
from datetime import datetime
import pandas as pd
from time import sleep


# Função para testar a velocidade de conexão da internet
def teste_internet():
    # Lendo a base de dados de testes anteriores
    df = pd.read_excel('C:\\Users\\55169\\Desktop\\teste_internet\\data.xlsx', sheet_name='base')
    
    # Instanciando a função de teste do Speedtest
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    
    # Testando velocidades de conexão
    velocidade_download = round(s.download(threads=None)*(10**-6))
    velocidade_upload = round(s.upload(threads=None)*(10**-6))
    
    # Capturando data e hora do teste
    data_atual = datetime.now().strftime('%d/%m/%Y')
    hora_atual = datetime.now().strftime('%H:%M')
    
    # Atualizando a base de dados dos testes
    df.loc[len(df)] = [data_atual, hora_atual, velocidade_download, velocidade_upload]
    df.to_excel('C:\\Users\\55169\\Desktop\\teste_internet\\data.xlsx', sheet_name='base', index=False)
    return data_atual, hora_atual, velocidade_download, velocidade_upload

# Definição de variáveis para teste
quantidade_testes = 1
segundos = 3
# Loop para execução dos testes
for q in range(quantidade_testes):
    data_atual, hora_atual, velocidade_download, velocidade_upload = teste_internet()
    print('Teste {}/{} Data: {} Hora: {} Download: {} Upload: {}'.format(q+1, quantidade_testes, data_atual, hora_atual, velocidade_download, velocidade_upload))    
    if (q+1) < quantidade_testes:
        sleep(segundos)