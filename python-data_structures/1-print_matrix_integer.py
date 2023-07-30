#!/usr/bin/python3
if __name__ == "__main__":
 def print_matrix_integer(matrix=[[]]):
   for row in matrix:
     for i in range(len(row)):
       if i == len(row) - 1:
         print("{}".format(row[i]))
       else: 
         print(row[i], end=", ")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_integer(matrix)
        
       

