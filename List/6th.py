l = list(map(int, input("Enter numbers: ").split()))
even_count = 0
odd_count = 0
for num in l:
    if num % 2 == 0:
        even_count =even_count + 1
    else:
        odd_count =odd_count + 1
diff = abs(even_count - odd_count)

print("Absolute difference:", diff)
