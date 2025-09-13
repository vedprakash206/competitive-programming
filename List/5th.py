# Write a program to print all negative numbers from input array A of size N
l = list(map(int, input("enter:").split()))
for num in l:
    if num < 0:
        print(num)

 

