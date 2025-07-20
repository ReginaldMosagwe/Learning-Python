            ### USER INPUT

## Input Strings
# relies on the input() method
print("Enter your First name: ")
fname = input() # Here, Python will stop executing until user has given some input
print(f"Hello {fname}")

# Using the prompt parameter of the input() fxn
sname = input("Enter your Surname: ") # The prompt and input appear on the same line unlike above
print(f"Hello {sname}")

## Input Number
# While needing input() for entry, the input needs the float() method to convert it to a number
import datetime

age = input("Enter your age:")
# find the year of birth
current = datetime.datetime.now()
YoB = current.year - float(age)

print(f"{fname} {sname}'s year of birth is {YoB}")
