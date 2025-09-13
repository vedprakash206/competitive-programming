# You are provided with an integer array A. Return another array B of size same as that of
#  A such that B[i] = A[i]^3 ina list.
A = list(map(int, input().split()))
B = [i**3 for i in A]
print(B)