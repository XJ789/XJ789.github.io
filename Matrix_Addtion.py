# Input Matrix A  
matrixA = [[int(input(f"Enter element ({i+1},{j+1}) of Matrix A: ")) for j in range(2)] for i in range(2)]  
# Input Matrix B  
matrixB = [[int(input(f"Enter element ({i+1},{j+1}) of Matrix B: ")) for j in range(2)] for i in range(2)]  
# Calculate Sum  
result = [[matrixA[i][j] + matrixB[i][j] for j in range(2)] for i in range(2)]  
# Display Result  
print("Sum:", result)  
