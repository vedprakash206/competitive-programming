emp = int(input())
ar = list(map(int, input().split()))
arr = []  
for i in ar:
    if i % 2 == 0:  
        arr.append(i)
if arr:  
    print(arr)
else:
    print(-1)
