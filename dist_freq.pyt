import pandas as pd

url = 'https://github.com/felipereis150/mod_sist/blob/main/distribuicao_de_freq.csv?raw=true'
df = pd.read_csv(url)
df.head(50)