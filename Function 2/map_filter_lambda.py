arr = [1, 2, 3, 4, 5, 6, 7]
squares = list(map(lambda x: x * x, arr))
ans = list(filter(lambda x: x % 4 == 0, squares))
print(ans)
