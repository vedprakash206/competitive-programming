num = float(input("Enter your percentage: "))
if num <= 25 :
    grade = "D"
elif num >=26 and num <= 45:
    grade = "C"
elif num >= 46 and num <= 65:
    grade = "B"
elif num >= 66 and num <= 85:
    grade = "A"
else:
    grade = "A+"
print("Your grade is:", grade)
