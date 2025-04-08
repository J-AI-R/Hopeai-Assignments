# ASSIGNMENT 1

#A1_3 BODY MASS INDEX

# - Underweight: BMI less than 18.5
# - Normal weight: BMI between 18.5 and 24.9
# - Overweight: BMI between 25 and 29.9
# - Obesity: BMI of 30 or greater

try:
    fv = float(input("Enter the BMI Index: "))
    bmi = float(fv)  # fv -> float value
    if (bmi < 18.5):
        print("Under weight")
    if (bmi >= 18.5 and bmi <= 24.9):
        print("Normal weight")
    if (bmi >= 25 and bmi <= 29.9):
        print("Over weight")
    if (bmi >= 30):
        print("Obesity")
except ValueError:
    print("Please enter a valid BMI Index")




