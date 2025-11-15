n=int(input())
a=list(map(int,input().split()))
L,R=map(int,input().split())
print(sum(a[L-1:R]))
