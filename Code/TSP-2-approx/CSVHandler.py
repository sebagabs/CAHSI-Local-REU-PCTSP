import csv


def transform_data(data_array):
    """Trasnform a matrix with String elements to one with integers."""
    transformed_data = []
    n = len(data_array)
    for row in range(0, n):
        temp = []
        for elem in range(0, n):
            temp.append(int(data_array[row][elem]))
        transformed_data.append(temp)
    return transformed_data

def read_csv_file(csv_file_name):
    """Reads the file `graph.csv` to obtain a graph as an adjacency matrix."""
    data_array = []  # Array to contain grades information.
    # Reads .csv file and adds information to data.
    with open(csv_file_name, 'r') as csv_file:
        scanner = csv.reader(csv_file)
        for line in scanner:
            data_array.append(line)
    adjacency_matrix = transform_data(data_array)
    return adjacency_matrix
