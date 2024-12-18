import numpy as np

def spiral(N, M):
    A = np.zeros((N, M))
    a = 1
    up = 0
    bottom = N - 1
    left = 0
    right = M - 1

    while up <= bottom and left <= right:
        for i in range(left, right + 1):
            A[up][i] = a
            a += 1
        up += 1

        for i in range(up, bottom + 1):
            A[i][right] = a
            a += 1
        right -= 1

        if up <= bottom:
            for i in range(right, left - 1, -1):
                A[bottom][i] = a
                a += 1
            bottom -= 1

        if left <= right:
            for i in range(bottom, up - 1, -1):
                A[i][left] = a
                a += 1
            left += 1

    print(A)
