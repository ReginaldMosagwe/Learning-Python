# PYTHON IF ... ELSE

# Mathematical logical conditions are commonly used in if-else statements to control the flow of a program. 
# Example: 

a = 10
b = 12

if b > a:
    print("b is greater than a") # Make sure with the indentation, otherwise ERROR!!!

###          # Elif keyword

a = 21
b = (((12 * 3) + 6) / 2)

if b > a:
    print("b is greater than a")
elif b == a:
    print("b is equal to a")

###      # Else keyword 
# The else keyword is used to execute a block of code when the if and elif conditions are not met.
# Also it is possible to have the else keyword without the elif keyword

a = 20
b = (((12 * 3) + 6) / 2)

if b > a:
    print("b is greater than a")
elif b == a:
    print("b is equal to a")
else:
    print("b is less than a")

# Using the technique known as Ternary Operators, or Conditional Expressions, one can have multiple else statements in a single line
# Foe Example:

print("b is greater than a") if b > a else print("=") if b == a else print("b is less than a")
# This is a more compact way to write if-else statements, but it can be less readable for complex conditions.

# LOGICAL AND Operator
# The logical AND operator (and) is used to combine multiple conditions.
# With 'and', if all conditions are true, the block of code inside the if statement will be executed.

a = 5 
b = 4 
c = 7
if a > b and c > b:
    print("It is an A and C showoff now!!")

# LOGICAL OR Operator
# The logical OR operator (or) is used to check if at least one of the conditions is true.
# If any of the conditions are true, the block of code inside the if statement will be executed.

a = 5 
b = 4 
c = 7
if a > b or b > c:
    print("At least one of the conditions is true! It will execute code block")

# LOGICAL NOT Operator
# The not Keyword is a logical operator used to reverse the result of the conditional statement
a = 5
b = 4

if not a < b:
    print("a is not less than b")


###                     # NESTED IF
# An if statement within another if statement is called nested if statements

x = 32

if x > 8:
    print("Above first multiple")
    if x > 16:
        print(" and also second multiple")
    else:
        print(" but not above 2nd multiple")

# PASS Statement
# if statements cannot be empty. 
# If the statement has no content, put in the pass statement to avoid errors

if a > b:
    pass # This will prevent the error of living the if statement empty


###                     #PYTHON MATCH STATEMENT
# Based on different conditions, the match statement is used to perform different actions
# It can be used as an alternative for multiple if...else statements
# The match statement selects one of many code blocks to be executed
# After evaluating the match expression once, the value of the expression is compared to the values of each case
# If there is a match, the associated code is executed


day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

# Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches

day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _: # This is the default case and should always come last as _ will always match
        print("Looking forward to the weekend")

# Also one can use the | (pipe character) as an or operator in the case evaluation to check for more than one value match  in one case
# Example:
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("Weekend is live!!")

# Additionally, you can use if statements as an extra condition check

month = 5
day = 2
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May!")
    case _:
        print("No match")

