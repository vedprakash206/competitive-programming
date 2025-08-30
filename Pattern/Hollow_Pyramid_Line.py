m=5
n=5
for i in range(m):
    for j in range(n):
        if j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()            