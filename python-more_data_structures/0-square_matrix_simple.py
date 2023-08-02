def square_matrix_simple(matrix=[]):
 
 new_matrix = []

 for row in matrix:
    new_row = []
    for value in row:
      new_value = value ** 2
      new_row.append(new_value)
 new_matrix.append(new_row)
 return new_matrix

