import pandas as pd

url = 'https://github.com/felipereis150/mod_sist/blob/main/primeira%20avalia%C3%A7%C3%A3o%20continuada/distribuicao_de_freq.csv?raw=true'
df = pd.read_csv(url)
df.head(5)
df['Sexo'].value_counts()
df['N Irmaos'].value_counts()
df['Discipl. Fav'].value_counts()