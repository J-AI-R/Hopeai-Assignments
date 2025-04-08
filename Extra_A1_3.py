"""
try:
    val = int(input('Guess a correct no.'))
    if val == 10:
        print("CORRECT")
except ValueError:
    print("Guess a correct no.")


try:
    pwd = str(input('Enter the password: '))
    if pwd == "HOPE@123":
        print("Your password is correct")
    else:
        print("Your password is incorrect")
except ValueError:
    print("Enter the password")

"""

#
