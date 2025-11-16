n=int(input())
l=list(map(int,input().split()))
target= int(input())
count=0
for i in range(n):
    for j in range(i+1,n):
        if l[i]+l[j]==target:
            count+=1
print(count)
