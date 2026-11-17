import numpy as np
def exact_value(P,r,gamma):
    n = len(r)
    A = np.eye(n) - gamma * P
    v = np.linalg.solve(A, r)       # YOU: solve A v = r
    return v


def neumann_value(P, r, gamma, K):
    n = len(r)
    total = np.zeros(n)
    term = r
    for p in range(K):
        total = total + term
        term = gamma * (P@ term)# YOU: the next term, made from this one
    return total


if __name__ == "__main__":
    P = np.array([[0.5, 0.5], [0.2, 0.8]])
    r = np.array([1.0, 0.0])
    v = exact_value(P, r, 0.9)
    print(np.max(np.abs(neumann_value(P, r, 0.9, 66) - v)))