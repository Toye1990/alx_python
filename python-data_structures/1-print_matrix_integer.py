def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    columns = len(matrix[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(columns):
            element = "{:d}".format(matrix[i][j])
            print(element, end=", ")
        print()

