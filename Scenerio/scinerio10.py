n = int(input())             
l = list(map(int, input().split()))
codes = []             
for i in range(n):
    count = 0
    for j in range(n):
        if l[i] == l[j]:
            count += 1
    if count == 1:            
        codes.append(l[i])   
if len(codes) == 0:
    print(-1)
else:
    print(*codes)            