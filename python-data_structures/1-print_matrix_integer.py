def print_matrix_integer(matrix=[[]]):
  for row in matrix:
    for element in row:
      print(str(element).rjust(4), end=" ")
    print()