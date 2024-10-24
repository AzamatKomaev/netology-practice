def min_breaks(n, m):
    if n == 1 and m == 1:
        return 0

    return n * m - 1

n = 3
m = 5
print(f'Min value for choko size {n} × {m} is: {min_breaks(n, m)}')
