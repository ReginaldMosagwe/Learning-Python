
# Try Except in Python
# An error is also known as an exceptionand is handled using the try statement

# try - let's you test a block of code for errors
# except - let's one handle the error
# else - let's you execute code when there is no error
# finally - let's you execute code, regardless of the result of try and except blocks

# Without a try block, if the program raises an error it will crash

            ## Exception Handling
try:
    print(x) # will raise an error if x is not defined
except:
    print("An exception occurred") # will be executed

# It is possible to have more than one exception - esp. when a special kind of error exists
#Exceptions can feature: ArithmeticError, Exception, SyntaxError, etc

try:
    print(x)
except NameError: # raised when a variable does not exist
    print("Variable x is not defined")
except:
    print("Something else is the problem")
else:
    print("Nothing went wrong") # OUTPUT: Nothing went wrong

            ## Else
# the else keyword defines a block to execute if no error is raised

            ## Finally
# will be executed regardless of try block raising an error or not.
# Below is a nested try except block

try:
    f = open("Hello.txt") # OUTPUT: Hello
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when trying to write the file") # Try block raises no exception, hence it not executed
    finally:
        f.close() # this is useful in closing objects and cleaning up resources 
except:
    print("Something went wrong when opening the file")

# Finally will allow the program to continue without leaving the file open

# As a programmer you can choose to throw an exception if certain conditions occur
# To throw/raise an exception use the raise keyword
# Example: 

x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")
if not type(x) is str:
    raise TypeError("It should be string here")