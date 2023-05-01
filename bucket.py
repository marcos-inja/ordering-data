import csv

def bucket_sort(file_path):
    # Leitura do arquivo CSV
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader) # armazena o cabeçalho
        rows = [row for row in reader] # armazena as linhas como uma lista de listas

    # Criação dos buckets vazios
    num_buckets = 10 # número de buckets
    buckets = [[] for _ in range(num_buckets)]

    # Adiciona cada linha ao bucket correspondente
    for row in rows:
        bucket_index = int(row[0]) % num_buckets # calcula o índice do bucket
        buckets[bucket_index].append(row)

    # Ordena cada bucket individualmente usando o método de ordenação de sua escolha
    for i in range(num_buckets):
        buckets[i].sort(key=lambda row: int(row[0])) # ordena pelo valor da coluna id convertido para inteiro

    # Concatena os buckets ordenados em uma única lista de linhas ordenadas
    sorted_rows = [row for bucket in buckets for row in bucket]

    # Escrita do arquivo CSV ordenado
    with open('sorted_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(sorted_rows)


bucket_sort('shuffled_data.csv')
