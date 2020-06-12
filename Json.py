'''
        Author : Arnob Mahmud

        Mail : arnob.tech.me@gmail.com
'''

import json

# some JSON:
x = '{ "name":"Arnob", "age":19, "city":"Dhaka"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
