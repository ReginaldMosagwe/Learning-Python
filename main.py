# How to go about importing
import platform
import datetime

x = platform.system()
print(x)
y = dir(platform)




                    ### DATETIME IN PYTHON
# Date and time objects in Python are obtainable in a module called datetime
x = datetime.datetime.now() # SYntax class.module.function()
print(x.year)
print(x.strftime("%A"))

# Creating date objects requires using the datetime() constructor, of the datetime module
# Ordinarily datetime requires 3 parameters (Year, Month, & Day)
# However, datetime() class also takes parameters for time & timezone (optional) with default value of 0 (None for timezone)


        ## Methods
# The strftime() method formats date objects into readable strings
#strftime() method takes one parameter, format, as shown below

print(x.strftime("%A %dth %b %Y %H%M HRS %z")) # strftime() only takes one argument You can edit the format and include things like HRS< Th etc

#NOTE: %a referes to weekday short version (Wed) while %A refers to weekday long version (Wednesday)
# The case of the letter invfluences the version