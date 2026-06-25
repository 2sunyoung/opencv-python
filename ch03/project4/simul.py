import numpy as np
A = np.array([[1,1,1,1],[2,-1,2,-1],[3,2,-1,2],[1,3,2,-1]])
B = np.array([10,3,11,9])

A_inv = np.linalg.inv(A)
print(f"\n계산된 역행렬(A_inv):\n{A_inv}")

solution = A_inv @ B

w, x, y, z = solution
print(f"역행렬을 이용한 방정식의 해:")
print(f"w = {w:.1f},x = {x:.1f},y = {y:.1f},z = {z:.1f}")
print(np.matmul(A, solution)) 
