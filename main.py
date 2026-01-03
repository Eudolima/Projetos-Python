import requests
import pandas as pd
from bs4 import BeautifulSoup

# 1. O robô visita o site
url = "https://ge.globo.com/futebol/futebol-internacional/futebol-ingles/"
resposta = requests.get(url)


# 2. O robô lê a página
site = BeautifulSoup(resposta.text, "html.parser")



# 3. O robô procura uma tabela (exemplo)


# 4. O robô salva no Excel

