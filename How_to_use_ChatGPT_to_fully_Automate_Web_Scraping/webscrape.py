"""
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro

Objetivo: Nest script fazemos uma raspagem de informações 
          num site da internet (imdb.com). Depois de coletar as 
          informações salvamos os Dados num arquivo CSV 🤗.

OBS: As vezes o site demora ou dá erro no retorno.
     Tente várias vezes a execução do script.          
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Definir o cabeçalho de usuário
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Recupere o conteúdo HTML do site
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
response = requests.get(url, headers=headers)
print(response)

# Analisar o conteúdo HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Encontre todos os elementos do filme
movies = soup.find_all('td', class_='titleColumn')


# Extract the desired information
data = []
for movie in movies:
    title = movie.find('a').text
    year = movie.find('span', class_='secondaryInfo').text
    data.append({'title': title, 'year': year})


# Criamos um DataFrame e salvamos em um CSV
df = pd.DataFrame(data)
print(df.head())
df.to_csv('imdb_top_movies.csv', index=False)
