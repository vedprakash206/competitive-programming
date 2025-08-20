n = int(input("\nEnter n: "))
if n % 3 == 0 and n % 10 == 4:
    print("Divisible by 3 and its last digit is 4")
else:
    print("It is not divisible by 3 and last digit is not 4")