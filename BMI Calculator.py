# This program will calculate a users body mass index
# by taking their body weight and using an
# algorithm to calculate the BMI.


weight = input("Please input your weight in lbs.")
height = input("Please input your height in inches.")
bmi = (int(weight) * 703 / int(height)) / int(height)

print(bmi)
print("A healthy BMI is 18.5 to 24.9")
print("An overweight BMI is 25 to 29.9")
print("An underweight BMI is anything less than 18.5")

if 18.5 <= bmi <= 24.9:
    print("You are at a healthy BMI.")
elif bmi > 25:
    print("You are at an overweight BMI.")
else:
    print("You are at an underweight BMI.")
