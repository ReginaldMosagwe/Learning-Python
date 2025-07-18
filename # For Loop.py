# FOR LOOP IN PYTHON

# For loop is used to iterate over a sequence (list, tuple, dictionary, set, or string)
# the for loop will execute a set of statements once for each item in the list. 

fruits = ["banana", "apple", "loquat"] # for lists and tuples
for x in fruits:
    print(x)

for x in "banana": #for string elements
    print(x)

# NOTE: Break works even in the for loop too

for x in fruits:
    print(x)
    if x == "apple":
        break #The result will be banana, apple & NO cherry

# Notice that in this case, after apple is printed is when the loop is exited
# Also, the break statement comes after the print() method

for x in fruits:
    if x == "apple":
        break
    print(x) # The result will be "banana" and NO apple and cherry

# In this case, the break statement comes before the print() method
# As such, the result will see an exit from the loop before "apple" is printed

# In the event that we do not want to print apple
for x in fruits:
    if x == "apple":
        continue
    print(x) # OUTPUT: banana & Cherry


                    # The range() function

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
# By default, the range() function increments the sequence by 1

for x in range(6): # NOTE: range is not the values 0-6 but instead 0-5
    print(x)

for x in range(2, 6): # Means values from 2 to 6 (including 2 but not 6) last inclusion is 5
    print(x)

# However, one can switch the increment to more than 1 by adding an extra parameter 

for x in range(2, 30, 3): # Features an increment of 3 for the sequence
    print(x) #OUTPUT:(2, 5, 8, 11, 14, 17, 20, 23, 26, 29)


                        # else in for loop
#else keyword in a for loop specifies a block of code to execute when the loop is finished.

for x in range(6):
  print(x)
else:
  print("Finally finished!")

# However, the else block will NOT be executed if the loop is stopped by a break statement
# it will execute if a continue statement is there instead of break

for x in range(6):
  if x == 3:
     break
  print(x)
else:
  print("Finally finished!") # Here it will not be executed.

                        # Nested for loop

# Refers to a loop within a loop
# The inner loop will be executed one time for each iteration of the outer loop
description = ["big", "tasty", "succulent"]
fruits = ["banana", "apple", "cherry"]

for x in description:
   for y in fruits:
      print(x, y) # OUTPUT: red apple, red banana, red cherry, big apple, big banana, big cherry, tasty apple, tasty banana, tasty cherry

                                        # The pass Statement
                    
# If you need a for loop with no content, use 'pass' to avoid errors
for x in range(3):
    pass #Having an empty 'for loop' would raise an alarm without the pass statement

