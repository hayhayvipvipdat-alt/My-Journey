x = int(input("What's your weight(kg) ? "))
y = float(input("What's your height(m) ? "))

bmi = x / (y ** 2)

if bmi >= 30:
    print("obese")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")

