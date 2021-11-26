A = range(1, 101, 1)
n = 100


def soma(n, A):
    if n == 0:
        s = 0
    else:
        s = soma(n - 1, A) + A[n - 1]
        print(s)
    return s


print(soma(n, A))
