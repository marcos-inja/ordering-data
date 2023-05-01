def from_csv_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return from_csv_string(content)

def from_csv_string(csv_string):
    lines = csv_string.strip().split('\n')
    return [line.split(',') for line in lines]

def to_csv_string(data):
    return '\n'.join([','.join(row) for row in data])

def quicksort(data):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    left = [x for x in data if x[0] < pivot[0]]
    middle = [x for x in data if x[0] == pivot[0]]
    right = [x for x in data if x[0] > pivot[0]]
    return quicksort(left) + middle + quicksort(right)

csv_list = from_csv_file('data.csv')
header, data = csv_list[0], csv_list[1:]
sorted_data = quicksort(data)
sorted_csv = to_csv_string([header] + sorted_data)

print(sorted_csv)