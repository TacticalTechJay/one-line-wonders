print([[sum([first_array[row1][col1] * second_array[col1][col2] for col1 in range(len(first_array[0]))]) for col2 in range(len(second_array[0]))] for row1 in range(len(first_array))])