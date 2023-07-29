def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    columns = len(matrix[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(columns):
            element = "{:d}".format(matrix[i][j])
            print(element, end=", ")
        print()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[1, 2, 3]]
matrix = [[1, 2, 3], [4, 5, 6]]
print_matrix_integer(matrix)