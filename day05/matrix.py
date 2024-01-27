def matrix_multiply(matrix1, matrix2):
    """
    Perform matrix multiplication for two matrices.
    
    Parameters:
    - matrix1 (list of lists): The first matrix.
    - matrix2 (list of lists): The second matrix.
    
    Returns:
    - list of lists: The result of matrix multiplication.
    - if matrix multiplication not possible return [] (empty list).
    """
    return []

if __name__ == '__main__':
    matrix_A = [[1, 2, 3], [4, 5, 6]]
    matrix_B = [[7, 8], [9, 10], [11, 12]]
    result_matrix = matrix_multiply(matrix_A, matrix_B)
    print("Result of matrix multiplication:")
    for row in result_matrix:
        print(row)
