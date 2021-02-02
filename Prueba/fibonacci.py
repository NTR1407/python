def fib(n):
    a, b = 0, 1
    if n == 1 or n == 0:
        print(1)
    else:
        while a < n:
            print(a, end=' ')
            a, b = b, a+b
        print()
fib(10)

