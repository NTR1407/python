






def bin(n):
    res = ''
    while n // 2 != 0:
        res = str(n%2)+res
        n = n // 2
    return str(n) + res
