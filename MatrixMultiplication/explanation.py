from matrixMultiplication import f as f1
from fastMatrixPow import f as f2


def matrixMultiplication(m1, m2):
    # Edge case
    if len(m1[0]) != len(m2):
        return None

    # Create the result matrix
    # Dimensions would be len(m1[0]) x len(m2)
    m3 = [[0 for row in range(len(m2))] for col in range(len(m1[0]))]

    for i in range(len(m1[0])):
        for j in range(len(m2)):
            for k in range(len(m1)):
                m3[i][j] += m1[i][k] * m2[k][j]
    return m3


def fastMatrixPow(m, n):
    if n == 1:
        return m
    x = matrixMultiplication(t := fastMatrixPow(m, n // 2), t)
    if n % 2:
        x = matrixMultiplication(x, m)
    return x



m1 = [[1, 2], [3, 4]]
m2 = [[5, 6], [7, 8]]

print(matrixMultiplication(m1, m2))
print(f1(m1, m2))

print(fastMatrixPow(m1, 10))
print(f2(m1, 10))
