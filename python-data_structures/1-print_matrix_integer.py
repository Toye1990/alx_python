def print_matrix_integer(matrix=[[]]):
 if not matrix:
    print("matrix empty")
    return
 
 for row in matrix:
   for element in row:
     print(element, end=" ")
   print()

