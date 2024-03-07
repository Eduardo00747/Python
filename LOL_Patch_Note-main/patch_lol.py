import requests
from bs4 import BeautifulSoup
import openpyxl

url = 'https://www.op.gg/champions'

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0 (Edition std-1)"}

site = requests.get(url, headers= headers)

soup = BeautifulSoup(site.content, 'html.parser')

# Encontrar a tabela que contém os dados dos campeões
table = soup.find('table', {'class':'css-12f3864 ezragh1'})

# Criar um arquivo Excel
wb = openpyxl.Workbook()
ws = wb.active

# Imprimir os cabeçalhos da tabela
headers = table.find_all('th')
header_names = [header.text.strip() for header in headers]
ws.append(header_names)

# Encontrar as linhas da tabela
rows = table.find_all('tr')

# Iterar sobre as linhas e extrair os dados
for row in rows[1:]:  # Começando do índice 1 para pular o cabeçalho
    cols = row.find_all(['td', 'th'])
    cols = [col.text.strip() for col in cols]
    print('\t'.join(cols))

# Iterar sobre as linhas e extrair os dados para o arquivo Excel
for row in rows[1:]:  # Começando do índice 1 para pular o cabeçalho
    cols = row.find_all(['td', 'th'])
    cols = [col.text.strip() for col in cols]
    ws.append(cols)

# Salvar o arquivo Excel na área do projeto
wb.save('dados_campeoes.xlsx')

