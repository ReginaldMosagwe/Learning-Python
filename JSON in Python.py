import json

# To convert a JSON string to Python, parse it using the json.loads() method
#JSON string:
x = '{"name": "Reggie", "age": 32, "city": "Nairobi"}'
#parse x:
y = json.loads(x) # result is a python dictionary

print(y["name"])
print(y["age"])

                ## Converting from python to JSON

# This conversion relies on the json.dumps() method

a = {"name": "Reggie", "age": 32, "city": "Nairobi"} # Dictionary in python
# Convert into JSON
b = json.dumps(a)
print(b) 

#Python objects that can be be converted into JSON (Javascript) strings:
# dict(Object), list(Array), tuple(Array), string(String), int(Number), float(Number), True(true), False(false), & None(null)

#The output is not very easy to read (No indentations and line breaks)
                ## Formating the Result

# Using the indent parameter
# here, consider b from above

c = json.dumps(a, indent=4, separators=(".", "=")) # will replace the , with a . and the : with = 
# In addition, one can order this result using the sort_keys parameter

d = json.dumps(a, indent=4, separators=(".", "="), sort_keys=True)
