# Create a function that checks whether the given number is Odd or Even
'''
class oddeven:
    def oddeven(num):
            if (num % 2) == 0:
                ret = "is Even number."
            else:
                ret = "is Odd number"
            return ret

try:
    # numb = float(input("Enter a number: "))
    numb = int(input("Enter a number: "))
    result = oddeven.oddeven(numb)
    print(numb, result)
except ValueError:
    print("Please enter a valid number")


# CHECK ELIGIBILITY

class EligiblityForMarriage:
    def Eligible(gen, age):
        eligiblit = ' '
        if gen == 'male':
            if age >= 21:
                eligiblit = "ELIGIBLE"
            else:
                eligiblit = "NOT ELIGIBLE"

        if gen == 'female':
            if age >= 18:
                eligiblit  = "ELIGIBLE"
            else:
                eligiblit = "NOT ELIGIBLE"

        return eligiblit


agevalid = ' '
genvalid = ' '

try:
    age = int(input("Enter your age: "))
    agevalid = 'Y'
except ValueError:
    agevalid = 'N'


if agevalid == 'Y':
    gen = input("Enter your gender: ")
    if gen.isalpha():
        genvalid = 'Y'
        gen = gen.lower()
    else:
        genvalid = 'Y'

if agevalid == 'Y' and genvalid == 'Y':
    eligible = EligiblityForMarriage.Eligible(gen,age)
    gen = gen.upper()
    print("Your Gender: ", gen)
    print("Your Age: ", age)
    print(eligible)
else:
    if agevalid != 'Y':
        print("Invalid age, please enter a valid number")
    elif genvalid != 'Y':
        print("Invalid gender, please use only alphabets")


# calculate the percentage of your 10th mark

class FindPercent:
    def percentage(total):
        percent = total / 5
        return percent

try:
    Sub1 = int(input("Enter subject 1 mark: "))
    Sub2 = int(input("Enter subject 2 mark: "))
    Sub3 = int(input("Enter subject 3 mark: "))
    Sub4 = int(input("Enter subject 4 mark: "))
    Sub5 = int(input("Enter subject 5 mark: "))
    total = Sub1 + Sub2 + Sub3 + Sub4 + Sub5
    percent = FindPercent.percentage(total)
    print("Percentage: ", percent)
except ValueError:
    print("Enter a valid mark in numbers")



class triangle:
    def areaoftriangle(h, b):
        area = (h * b) / 2
        return area

    def perimeteroftriangle (s1, s2, s3):
        peri = s1 + s2 + s3
        return peri

try:
    height = float(input("Input the height of triangle: "))
    breadth = float(input("Input the breadth of triangle: "))
    area = triangle.areaoftriangle(height,breadth)

    a = float(input("Input the side 1 of triangle: "))
    b = float(input("Input the side 2 of triangle: "))
    c = float(input("Input the side 3 of triangle: "))
    perimeter = triangle.perimeteroftriangle(a, b, c)

    print("Area of Triangle: ", area)
    print("Perimeter of Triangle: ", perimeter)
except ValueError:
    print("Enter a numeric value")


'''

def test():
    return 5
print(test() + 10)

