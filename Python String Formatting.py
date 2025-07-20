# Python String Formatting

        ## F-Strings

# f-strings allows one to format select parts of a string

txt = f"The price of a Crate of Eggs is 450 shillings"
print(txt)

# placeholders {} are useful for formatting an f-string
# placeholders can contain variables, operations, functions, and modifiers
price = 450
txt = f"The price of a Crate of Eggs is {price} shillings" # {price} is the placeholder
print(txt)

# these placeholders can also include a modifier to format the value
# A modifeir is included by adding a colon : followed by a formatting type like .2f

txt = f"The price of a Crate of Eggs is {price:.2f} shillings" # {price:.2f} here price is the placeholder and modier is .2f
print(txt)

#ALTERNATIVELY
txt = f"The price of a Crate of Eggs is {450:.2f} shillings" # To format the value directly

            ## Operations in F-Strings]
# It is possible to perform mathematical operations within the placeholder and return results
txt = f"The price of a Crate of Eggs is {price} shillings"
units = 30
unit_price= (f"The cost of an egg is {(price/30)-((price/30)*0.16)}")

# Furthermore, placeholders can have an if... else statement
remark = (f"The cost of an egg is {'Expensive' if unit_price > 13 else 'Cheap'}")
print(remark.upper())
