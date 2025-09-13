#  You are given a constant array A and an integer B.
#  You are required to return another array where Arr[i] = A[i] + B.
l=list(map(int,input("enter:").split()))
b=int(input("enter:"))
for i in range(len(l)):
    l[i]=l[i]+b
print(l)
