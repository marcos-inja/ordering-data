import csv

# Função para aplicar o algoritmo Radix Sort
def radix_sort(lst):
    RADIX = 10
    max_length = False
    temp, placement = -1, 1

    while not max_length:
        max_length = True
        buckets = [list() for _ in range(RADIX)]
        for i in lst:
            temp = i[0] // placement
            buckets[temp % RADIX].append(i)
            if max_length and temp > 0:
                max_length = False

        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                lst[a] = i
                a += 1

        placement *= RADIX
    return lst

# Lendo o arquivo data.csv
with open("shuffled_data.csv", "r") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    data = [row for row in csv_reader]

# Ordenando pela coluna "Id" utilizando Radix Sort
data = radix_sort([(int(row[0]), row) for row in data])
sorted_data = [row[1] for row in data]
print(sorted_data[0])

# Escrevendo o resultado em um novo arquivo CSV
with open("sorted_data.csv", "w", newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(header)
    csv_writer.writerows(sorted_data)
