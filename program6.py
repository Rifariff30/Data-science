import numpy as np
r1 = int(input("enter rows for matrix A: "))
c1 = int(input("enter columns for matrix A: "))
print(f"enter {r1} rows (numbers separated by spaces):")
A = np.array([[float(x) for x in input(f"row {i+1}: ").split()] for i in range(r1)])
r2 = int(input("\nenter rows for matrix B: "))
c2 = int(input("enter columns for matrix B: "))
print(f"enter {r2} rows (numbers separated by spaces):")
B = np.array([[float(x) for x in input(f"row{i+1}: ").split()] for i in range(r2)])
print(f"\nmatrix A:\n{A}\n\nmatrix B:\n{B}\n")
if A.shape == B.shape:
    print(f"Addition (A + B):\n{A+B}\n")
else:
    print("Addition not possible (Dimensions must match).\n")
if c1 == r2:
        print(f"Multiplication(A @ B):\n{A@B}\n")
else:
        print("Multiplication not possible(columns of A must equal rows of B).")
