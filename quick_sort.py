import csv


# Função de partição para o quicksort
def partition(data, low, high):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j][0] <= pivot[0]:
            i += 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1


# Algoritmo quicksort
def quicksort(data, low, high):
    if low < high:
        pi = partition(data, low, high)
        quicksort(data, low, pi - 1)
        quicksort(data, pi + 1, high)


# Leitura do arquivo CSV
filename = "shuffled_data.csv"
rows = []

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        row[0] = int(row[0])
        rows.append(row)

# Ordenação usando quicksort
quicksort(rows, 0, len(rows) - 1)

# Salvar arquivo CSV ordenado
with open("sorted_data.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerows(rows)
