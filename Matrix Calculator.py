# Function to create a matrix of given size
def create_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            element = float(input("Enter element: "))
            row.append(element)
        matrix.append(row)
    return matrix

# Function to print a matrix
def print_matrix(matrix):
    for row in matrix:
        print(row)

# Function to add two matrices
def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = matrix1[i][j] + matrix2[i][j]
            row.append(element)
        result.append(row)
    return result

# Function to subtract two matrices
def subtract_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = matrix1[i][j] - matrix2[i][j]
            row.append(element)
        result.append(row)
    return result

# Function to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if cols1 != rows2:
        print("Cannot multiply the matrices. Invalid dimensions.")
        return None

    result = []
    for i in range(rows1):
        row = []
        for j in range(cols2):
            element = 0
            for k in range(cols1):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result.append(row)
    return result

# Function to transpose a matrix
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for j in range(cols):
        row = []
        for i in range(rows):
            element = matrix[i][j]
            row.append(element)
        result.append(row)
    return result

# Main calculator loop
while True:
    print("Matrix Calculator")
    print("1. Add matrices")
    print("2. Subtract matrices")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        print("Addition")
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        print("Enter the elements of the first matrix:")
        matrix1 = create_matrix(rows, cols)
        print("Enter the elements of the second matrix:")
        matrix2 = create_matrix(rows, cols)
        result = add_matrices(matrix1, matrix2)
        print("Matrix Addition is shown as:")
        print_matrix(result)
    elif choice == '2':
        print("Subtraction")
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        print("Enter the elements of the first matrix:")
        matrix1 = create_matrix(rows, cols)
        print("Enter the elements of the second matrix:")
        matrix2 = create_matrix(rows, cols)
        result = subtract_matrices(matrix1, matrix2)
        print("Result:")
        print_matrix(result)
    elif choice == '3':
        print("Multiplication")
        rows1 = int(input("Enter the number of rows of the first matrix: "))
        cols1 = int(input("Enter the number of columns of the first matrix: "))
        rows2 = int(input("Enter the number of rows of the second matrix: "))
        cols2 = int(input("Enter the number of columns of the second matrix: "))
        if cols1 != rows2:
            print("Cannot multiply the matrices. Invalid dimensions.")
            continue
        print("Enter the elements of the first matrix:")
        matrix1 = create_matrix(rows1, cols1)
        print("Enter the elements of the second matrix:")
        matrix2 = create_matrix(rows2, cols2)
        result = multiply_matrices(matrix1, matrix2)
        if result:
            print("Result:")
            print_matrix(result)
    elif choice == '4':
        print("Transpose")
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        print("Enter the elements of the matrix:")
        matrix = create_matrix(rows, cols)
        result = transpose_matrix(matrix)
        print("Result:")
        print_matrix(result)
    elif choice == '5':
        print("Exiting the Matrix Calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
