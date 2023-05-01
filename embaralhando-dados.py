import pandas as pd

# Ler o arquivo csv em um objeto pandas DataFrame
data = pd.read_csv('data.csv')

# Classificar os dados usando o algoritmo quicksort
sorted_data = data.sort_values(by=['Name'])

# Salvar o DataFrame classificado com índice em um novo arquivo CSV
sorted_data.to_csv('sorted_data.csv', index=True)

# Embaralhar o DataFrame classificado
shuffled_data = sorted_data.sample(frac=1, random_state=42)

# Salvar o DataFrame embaralhado com índice em um novo arquivo CSV
shuffled_data.to_csv('shuffled_data.csv', index=True)
