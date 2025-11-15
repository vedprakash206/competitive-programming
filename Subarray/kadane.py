n=int(input())
a=list(map(int,input().split()))
curr=a[0]
ans=a[0]
for i in range(1,n):
    curr=max(a[i],curr+a[i])
    ans=max(ans,curr)
print(ans)
