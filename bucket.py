import csv

def bucket_sort(arr):
    min_id = min(arr)
    max_id = max(arr)
    bucket_count = max_id - min_id + 1
    buckets = [[] for _ in range(bucket_count)]

    for i in arr:
        idx = i - min_id
        buckets[idx].append(i)

    sorted_arr = []
    for bucket in buckets:
        if bucket:
            sorted_arr.extend(bucket)

    return sorted_arr

filename = 'shuffled_data.csv'

with open(filename, newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)
    rows = [row for row in csv_reader]

rows.sort(key=lambda x: int(x[0]))  # Ordena por ID

with open('sorted_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(header)
    for row in rows:
        csv_writer.writerow(row)
