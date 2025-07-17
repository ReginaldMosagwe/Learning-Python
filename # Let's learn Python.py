# Let's learn Python
# There are numerous groups of operators: Arithmetic, Assignment, 
# Logical, Comparison, Bitwise, Identity, & Membership operators.\



# First off we deal with Arithmetic Operators
print("Arithmetic Operators:")

x = 50
y = 5

print("Addition: X + Y =", x + y)
print("Subtraction: X - Y =", x - y)
print("Multiplication: X * Y =", x * y)
print("Division: X / Y", x / y)
print("Modulus: X % Y =", x % y)
print("Exponentiation: X ** Y =", x ** y)
print("Floor Division: X // Y =", x // y)

print("Assignment Operators:")

x = 1.0
print(x)
x += 3
print(x)
x -= 3
print(x)
x *= 2
print(x)
x /= 2
print(x)
x %= 2
print(x)
x //= 2 #Floor division performs a division and returns the largest whole integer <= the result
print(x)
x **= 3 #more like x to the power of 3
print(x)

print(x := 2) #Assigns a value to a variable as part of an expression 

print("Logical Operators:")

# Logical conditions are often used in conditional/control flow statements
# and returns true if both conditions are met
# or returns true if at least one condition is met
# not returns true if the condition is false
x = 5
y = 8

print("X and Y:", x>4 and y<9)
print("X or Y:", x>4 or y<6)
print("not X:", not x>4)

print("Comparison Operators are similar to their function in mathematics")
# They are used to compare two values and return a boolean result
# They are often used in conditional statements and loops
# Tey can also be used to sort data structures like lists and tuples
# They include: ==, !=, >, <, >=, and <=

print("Identity operators:")
# These are used to compare the memory location of two objects
# They return true if both objects are the same object in memory
x = [1, 2, 3]
y = [1, 2, 3]
x is y
x is not y

print("Membership Operators:")
#Used to check the presence of a value in a sequence(list, tuple, string)
# Include in and not in
x = [1, 2, 3, 4, 5]
print("1 in x:", 1 in x)
print("6 not in x:", 6 not in x)
# These operators will return True or False based on the presence of the value in the sequence
# They are often used in conditional statements and loops

# OPERATOR PRECEDENCE
#Operators have a precedence that determines the order in which they are evaluated
# The order of precedence is as follows:
#   1. Parenthesees ()
print((6*3)+(5-1))
#   2. Exponentiation **
print(6**3+(5-1))
#   3. Unary plus and minus + -
print(100+ -1)
#   4. Multiplication, Division, Floor Division, and Modulus *, /, //, %
print((6*3)+(5/1)-(4//2) *(10%4))
#   5. Addition and Subtraction + -
print((6*3)+(5/1)-(4//2) *(10%4)+100-1)
#   6. Bitwise Shift Operators << and >>]
print((6*3)+(5/1)-(4//2) *(10%4)+100-1<<2)
#   7. Bitwise AND &
print((6*3)+(5/1)-(4//2) *(10%4)+100-1<<2 & 2)
#   8. Bitwise XOR ^
print((6*3)+(5/1)-(4//2) *(10%4)+100-1<<2 & 2 ^ 3)
#   9. Bitwise OR |
print((6*3)+(5/1)-(4//2) *(10%4)+100-1<<2 & 2 ^ 3 | 4)
#   10. Comparison Operators <, <=, >, >=, ==, !=
print((6*3)+(5/1)-(4//2) *(10%4)+100-1<<2 & 2 ^ 3 | 4 < 5)
#   11. Identity Operators is, is not
print((6*3)+(5/1)-(4//2) *(10%4)+100-1<<2 & 2 ^ 3 | 4 < 5 is True)
#   12. Membership Operators in, not in
print((6*3)+(5/1)-(4//2) *(10%4)+100-1<<2 & 2 ^ 3 | 4 < 5 is True in [True, False])
#   13. Logical Operators and, or, not
print((6*3)+(5/1)-(4//2) *(10%4)+100-1<<2 & 2 ^ 3 | 4 < 5 is True in [True, False] and True)


#                       PYTHON LISTS
# Lists are a collection of items that are ordered, changeable, and stored in a single variable.
# Lists can contain any data type, including other lists, and can be nested.
# These Lists are defined using square brackets [] and can be accessed using indexing.
# Lists are created using square brackets []

thislist = ["a", 2, 3.1, True, (1, 2, 3), "hello", [1, 2, 3]]
print("This is a list:", thislist)
print("The first item in the list is:", thislist[0])
print("The last item in the list is:", thislist[-1]) # Negative indexing means start from the end of the list
# The Second, Third, ...items are [1], [2], ... and so on
#  Lists are ordered, and that order will not change. The last added will appear at list's end
# One can change, add, and remove list items after list creation. 
# Also, lists can contain duplicate items.
# # To determine list length, use the len() function
print(len(thislist))
# This returns the number of list items in the list, in our case, it returns 7
# Lists are defined as objects with datatype 'list'
print(type(thislist))
# You can change the item indexed in a list as follows:
thislist[0] = "z"
print(thislist) # will return; thislist = ['z', 2, 3.1, True, (1, 2, 3), 'hello', [1, 2, 3]]

print(thislist[:4]) # Will begin from the start of the list and return the first four items
print(thislist[2:]) # Will return the lsit from the third item to the end
thislist[1:2] = [17, "wewe"]
print(thislist) # Will return thislist = ["z", 17, "wewe", 3.1, True, ...]
# Thus the immediate above moves will result in the list length increasing by one item
 # Other than lists, other arrays in Python include tuples, sets, and dictionaries.
# Inserting an Item to the List
thislist.insert(2, "mimi")
print(thislist) # Will return thislist = ["z", 17, "mimi", "wewe", 3.1, True, (1, 2, 3), 'hello', [1, 2, 3]]
thislist.append("newItem")
print(thislist) # Will return thislist = ["z", 17, "mimi", "wewe", 3.1, True, (1, 2, 3), 'hello', [1, 2, 3], 'newItem']
# Append() function will add a new item to the end of the list
thislist.remove("newItem") # Will remove the first occurrence of the item in the list

thislist.pop(2) # Will remove the item at index 2
thislist.pop() # Will remove the last item in the list

del thislist[2] # Will delete the item at index 2
del thislist # Will delete the entire list

thislist.clear() # Will remove all items in the list, but the list will still exist


# LOOPING IN LISTS
# To loop through and print each item in the list, use for loop

thislist = [1, "Reginald", 3.14, True, [1, 2, 3], (4, 5, 6)]

# USING A FOR LOOP
for x in thislist:
    print(x) # Will print each item in the list

# By refering to the index number, you can also loop through the list
for x in range(len(thislist)): # When including Range, the start index, i.e., [2] is included but the end index, i.e., [5] is not
    print(thislist(x))

#USING A WHILE LOOP
x = 0
while x < len(thislist):
    print(thislist[x])
    i = i + 1

    # USING LIST COMPREHENSION
thislist = [1, "Reginald", 3.14, True, [1, 2, 3], (4, 5, 6)]
[print (x) for x in thislist]

daylist = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
newlist = []
for x in thislist:
    if "t" in x:
        newlist.append(x)
        print(newlist) #Will print the items in the list that contain the letter "t", i.e., ["Tuesday", "Thursday", "Saturday"] in newlist

# However, you can shorten this process with list comprehension
newlist = [x for x in daylist if "t" in x]
print(newlist) # Will print the items in the list that contain the letter "t", i.e., ["Tuesday", "Thursday", "Saturday"] in newlist
# The Syntax is:
    # [expression for item in iterable if condition]
    # Example:
    # newlist = [x for x in daylist if "t" in x]

#CONDITIONS
# Conditions are used to perform filtration since it only accepts items that evaluate to TRUE
#An iterable can be a list, tuple, dictionary, set, or range() function
# The expression is the current item in the iteration, but is also the outcome
# The expression can be manipulated before being returned to the new list
newlist = [x.upper() for x in daylist if "t" in x]
print(newlist)

newlist = [x if x != "Monday" else "FUDGE!!" for x in daylist] #Will replace "Monday" with "FUDGE!!"

# SORT LIST

# The sort() method sorts list objects alphanumerically, ascending by default
thislist = ["apple", "banana", "cherry", "date", "orange", "kiwi", "pineapple", "mango"]
thislist.sort()
print(thislist) # Will print the sorted list in ascending order

thislist.sort(reverse = True)
print(thislist) # Will print the sorted list in descending order

def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) # Will sort the list based on its closeness to 50

# By default sort() method is case sensitive, meaning that uppercase letters will be sorted before lowercase letters
# T oignore case sensitivity, use the key parameter with str.lower
fruits = ["banana", "Orange", "Kiwi", "cherry"]

fruits.sort() # Will return ['Kiwi', 'Orange', 'banana', 'cherry'] # This takes into account case sensitivity
fruits.sort(key = str.lower) # Will return ['banana', 'cherry', 'Kiwi', 'Orange'] # This ignores case sensitivity

#COPYING IN PYTHON LISTS

# The copy() method returns a copy of any list.
# Example:
fruits = ["banana", "Orange", "Kiwi", "cherry"]
matunda = fruits.copy()
print(matunda) # Will print out ['banana', 'Orange', 'Kiwi', 'cherry']

# ALTERNATIVELY, one might use the list() constructor to copy a list
matunda = list(fruits)
print(matunda) # Will print out ['banana', 'Orange', 'Kiwi', 'cherry']
# However, this method will not work for nested lists, as it will only copy the outer list
# To copy a nested list, use the copy() method or the list() constructor

# LASTLY, one can use the slicing method to copy a list
matunda = fruits[:]
print(matunda) # Will print out ['banana', 'Orange', 'Kiwi', 'cherry']
# However, this method will not work for nested lists, as it will only copy the outer list
# To copy a nested list, use the copy() method or the list() constructor

#JOINING TWO LISTS

# The + operator can be used to join or concatenate two lists
list1 = ["apple", "banana", "cherry"]
list2 = ["orange", "kiwi", "mango"]
list3 = list1 + list2
print(list3) # Will print out ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']

# The extend () method can also be used in joining or concatenating two lists
list1 = ["apple", "banana", "cherry"]
list2 = ["orange", "kiwi", "mango"]
list1.extend(list2)
print(list1) # Will print out ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']
# The extend() method will add the items of the second list to the end of the first list

# The append() method can also be used to add a list to another list
list1 = ["apple", "banana", "cherry"]
list2 = ["orange", "kiwi", "mango"]
list1.append(x for x in list2)
print(list1) # Will print out ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']
# The append() method will add the entire list as a single item to the end of the list

### Range and Negative Indexes
list3 = list1 + list2
print(list3) # Will print out ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']

marketable_list = list3[-5:-1] # Will include index -5 (Orange) and exclude index -1 (Mango)
print(marketable_list) # Will print out ['banana', 'cherry', 'orange', 'kiwi']



## TUPLES

# A tuple has round braces () while a list has square braces []
# A tuple can have one or more items, but it is immutable (cannot be changed)

thistuple = ("apple",) # A tuple with one item must have a comma after the item
print(type(thistuple))

anothertuple = ("banana", "cherry", "orange")
print(anothertuple)

### Workarounds for TUPLES
# Tuples are immutable, meaning that once created, they cannot be changed
# However, you can convert a tuple to a list, change the list, and then convert it back to a tuple
# Example:

x = ("banana", "cherry", "apple") #tuple
y = list(x) #convert tuple to list
y[1] = "kiwi" #change the list
x = tuple(y) #convert list back to tuple
print(x) # Will print out ('banana', 'kiwi', 'apple')

## ALSO, one can add a tuple to another tuple using the + operator
x = ("banana", "cherry", "apple")
y = ('ochanda',) # Remember a one-item tumple requires the comma & tpe of quote does not matter
x += y # this will add the second tuple to the first tuple
print(x) # Will print out ('banana', 'cherry', 'apple', 'ochanda')

## To remove, append, or change items in a tuple in any way, one must convert the tuple to a list, make the changes, and then convert it back to a tuple

# Assigning values to a tuple is called packing while unpacking is the process of extracting values from a tuple into variables
fruits = ("apple", "banana", "cherry") # Packing
(fruit1, fruit2, fruit3) = fruits # Unpacking
print(fruit1) # Will print 'apple'
print(fruit2) # Will print 'banana'
print(fruit3) # Will print 'cherry'
########## NOTE: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

## LOOPING THROUGH TUPLES

# You can loop through a tuple using a for, while, and index numbers loop
# Using a for loop
for x in fruits:
    print(x) # Will print each item in the tuple

#Using a while loop
i = 0
while i < len(fruits): # 
    print(fruits[i]) # Will print each item in the tuple
    i += 1 # Increment the index by 1

# Using index numbers
for i in range(len(fruits)):
    print(fruits[i]) # Will print each item in the tuple

# Using list comprehension
fruits = ("apple", "banana", "cherry")
[print(x) for x in fruits] # Will print each item in the tuple

## One can add and multiply tuples using the + and * operators
# Adding tuples
tuple1 = ("apple", "banana", "cherry")
tuple2 = ("orange", "kiwi", "mango")
tuple3 = tuple1 + tuple2
print(tuple3) # Will print out ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango')

# Multiplying tuples
tuple1 = ("apple", "banana", "cherry")
tuple2 = tuple1 * 3
print(tuple2) # Will print out ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry', 'apple', 'banana', 'cherry'),
# The * operator will repeat the tuple the specified number of times

# del tuple2 will delete the entire tuple
del tuple2


#   ## SETS

# A set is a collection of unique items that are unordered, unchangeable, unindexed, and do not allow duplicates.
# Sets are defined using curly braces {} or the set() constructor
thisset = {"apple", "banana", "cherry"}
print("This is a set:", thisset)
# Sets are unordered, meaning that the items have no index and cannot be accessed by index number
#The values 'True' and 1 are considered the same in a set, as are 'False' and 0 (Considered duplicate items)
# Once a set is created, you cannot change its items, but you can add and remove items
# To determine the length of a set, use the len() function

# To add an item to a set, use the method add()

thisset = {"one", "two", "three"}
thisset.add("four") # Will add "four" to the set
print(thisset) # Will print out {'one', 'two', 'three', 'four'}

# To add multiple items (Another set, tuple, list, or dictionary) to a set, use the update() method

riley = {"five", "six", "seven"} #This can be a set, tuple, list, or dictionary
thisset.update(riley) # Will add all items in the riley set to thisset
print(thisset) # Will print out {'one', 'two', 'three', 'four', 'five', 'six', 'seven'}

