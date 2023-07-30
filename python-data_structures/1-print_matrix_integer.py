#!/usr/bin/python3
if __name__ == "__main__":
 def print_matrix_integer(matrix=[[]]):
   for row in matrix:
     for i in range(len(row)):
       if i == len(row) - 1:
         print(row[i])
       else: 
         print(row[i], end=", ")
       

