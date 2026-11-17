import numpy as np
from values import exact_value, neumann_value

P = np.array([[0.5, 0.5], [0.2, 0.8]])
r = np.array([1.0, 0.0])
A = np.eye(2) - P
print("rank", np.linalg.matrix_rank(A), "cond", np.linalg.cond(A))
for K in (10, 100, 1000):
    print(K, neumann_value(P, r, 1.0, K))
print("solve", exact_value(P, r, 1.0))
