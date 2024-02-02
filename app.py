import numpy as np

# Read the dimensions N and M
N, M = map(int, input().split())

# Read the arrays A and B from input
A = np.array([input().split() for _ in range(N)], dtype=int)
B = np.array([input().split() for _ in range(N)], dtype=int)

# Perform and print the required operations
print(np.add(A, B))          # Element-wise addition
print(np.subtract(A, B))     # Element-wise subtraction
print(np.multiply(A, B))     # Element-wise multiplication
print(np.floor_divide(A, B)) # Element-wise floor division
print(np.mod(A, B))          # Element-wise modulo
print(np.power(A, B))        # Element-wise exponentiation
