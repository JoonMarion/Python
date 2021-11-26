A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 10

def soma (k, n, A):
    if k > n-1:
        s = 0
    else:
        s = A[k] + soma(k+1, n, A) 
        print(s)
    return s

print(soma(0, n, A))  