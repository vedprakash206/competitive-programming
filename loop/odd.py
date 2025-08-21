n = int(input("enter a number"))
for i in range(2, n + 1, 2):
    print(i)
    if i % 2 != 0:
        print("Odd number found:", i)