# https://python.datalumina.com/


# import requests

# # Download a web page
# response = requests.get("https://api.github.com")
# print(response.status_code)  # Should print 200

# print("hello world")

"""
multi line comment
"""


name = "Alice"


is_student = True

for i in range(1,6):
        print (i)

age =25

#list
my_list = ["Alice",25,age,True]
print(my_list[0])
print(my_list[-2])
my_list.append(66)

# dictionary
person = {
    "name": "Alice",
    "age": 25
}

person["name"]
person["city"] = "Ashdod"
del person["city"]

person.keys()
person.values()
person.items()

if "name" in person:
    print("Not found")

person.update({"age":1,"citi":"TA"})

#Tuples
empty=()
point=(3,5) 
colors = ("Red","Green","Blue")

print(colors(0))

#sets

empty_set = set()
numbers = {1,2,3,4,5}
scores =[85,90,85,92,90];
unique_scores = set(scores)
print(unique_scores)

#==================================
#functions

def greet():
    print("Hello")

greet()


def greet(name):
    print(f"Hello, {name}!")

# defaukt values at the end
def introduce(name, age=33):  
    print(f"My name is {name}")
    print(f"I am {age} years old")

introduce("shlomi",55)

def add_print(a,b):
    print(a + b)
    return a+b

add_print(3,5)
result = add_print(6,7)

# return multi values
def simple_func():
    numbers = [1,2,3,4,5]
    first_number = numbers[0]
    last_number = numbers[-1]
    return first_number,last_number


first,last = simple_func()

#================================
#packages

# Pattern 1: Import the whole module
import math
# Now use: math.sqrt(16)
math.sqrt(16)

# Pattern 2: Import specific items from a module
from math import sqrt, pi
# Now use: sqrt(16)

import random
num = random.randint(1,10)
choice = random.choice(["apple", "banana","orange"])

import datetime
today = datetime.date.today()
print(today)  # 2024-01-15

# Operating system
import os
current_dir = os.getcwd()
print(current_dir)

# JSON data
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
print(json_string)


# Import with alias
import random as rnd
df = rnd.gauss




# Install a package
#pip install requests

# Install specific version
#pip install requests==2.28.0

# Install multiple packages
#pip install pandas numpy matplotlib


#### shared the rpoject
    # run pip freeze > requirements.txt
    # created requirementrs.txt
    # install this file - pip install -r requirements.txt


# =================I


import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)
print(data["current"])
print(data["current"]["temperature_2m"])
#-----

import requests

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

# Get temperature for different cities
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)

print(f"Paris: {paris_temp}°C")
print(f"London: {london_temp}°C")
print(f"Tokyo: {tokyo_temp}°C")





































