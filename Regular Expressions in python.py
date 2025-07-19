# When working with regular expressions import the built-in regex module called re

import camelcase
import re

txt = "This is Kenya"
x = re.search("^This.*Kenya$", txt)

if x:
    print("Yes! We have a match")
else:
    print("No match!-")

c = camelcase.CamelCase()

print(c.hump(txt)) # This method capitalizes the first letter of each word


# Other than search function, others exist including: 
# re.findall(), re.search(), re.split(), & re.sub()