number = int(input("Enter marks: "))

if number <= 25:
    print("Grade: D")
elif number>=25 and number<=45:
    print("Grade: C")
elif number>= 45 and number<=65:
    print("Grade: B")
elif number>=65 and number<=85:
    print("Grade: A")
elif number>=85:
    print("Grade: A+")