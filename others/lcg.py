def my_lcg(M, A, B, x0, N):
    x = x0
    for i in range(N):
        x = (A * x + B) % M
        print(x)

my_lcg(11, 2, 7, 8, 3)