def fun(a):
    return a % 2 == 0

sequence = [1, 2, 3.0, 4.5, 6, 8]
filtered = list(filter(fun, sequence))
print(filtered)
