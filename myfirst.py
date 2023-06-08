import random
print("Hi Raj")
ran_num = random.random()
print (ran_num)
resp = random.choice([1,2,3,4,6])
print(resp)

import requests
response = requests.get("http://www.google.co.uk") #wget curl
#print (response.content)


#bot_number_one.py
import random
player_options = ['R','P','S','D','W']
#def make_move(rounds):
def make_move():
    chosen_move = random.choice(player_options)
    print("Chosen move is: " + chosen_move)
    print("Chosen move is: " + random.choice(player_options))
    return chosen_move

make_move()

whisper = 'hello, world'
shout = whisper.upper()
print(shout.lower())

def p(input):
    print(input)

my_list = [1, 4, 5, 2, 3]
my_list.sort() #sort my list array
p(my_list)

def print_total_interest(initial_loan, interest_rate, number_of_years):
    repayment_amount = initial_loan * (interest_rate ** number_of_years)
    total_interest = repayment_amount - initial_loan
    print(f'£{total_interest:.2f}')
    print(f'£{total_interest}')

print_total_interest(1000, 1.05, 10)
print_total_interest(number_of_years=7, initial_loan=1000, interest_rate=1.07) #unordered vars, use names

def get_total_interest(initial_loan, interest_rate, number_of_years):
    repayment_amount = initial_loan * (interest_rate ** number_of_years)
    return repayment_amount - initial_loan

interest = get_total_interest(1000, 1.05, 10)
print(interest)


#make_move
#python ./bot_runner.py ./bot_number_one.py 
#python ./bot_runner.py ./bot_number_one.py ./example_class_bot.py

def greet(name):
    p('Hello ' + name)

greet('Me')
name_one = 'Jane'
name_two = 'Joe'
greet(name_one)
greet(name_two)

def sort_list_ret_1st_alpha(list):
    list.sort()
    return list[0]

p(sort_list_ret_1st_alpha(['beta', 'gamma', 'alpha']))

def make_a_sandwich(filling):
    filling='bacon'
    sandwich = ['bread', filling, 'bread']
    print(sandwich)
    return sandwich

my_sandwich = make_a_sandwich('cheese')
p(my_sandwich)

def do_nothing():
    pass # functions cant be empty use placeholder 'pass'

do_nothing()

def my_function():
    print('My function has run')

def call_it_twice(function):
    function()
    function()

call_it_twice(my_function)

it_is_raining = True

if it_is_raining:
    print('bring an umbrella')

def clap_your_hands():
    p('Clap, clap!')
you_are_happy = True
you_know_it = True 
if you_are_happy and you_know_it:
    clap_your_hands()    

#treated as false: 0 , An empty string: '' , An empty collection, like [] or {} , None
if len(my_list) > 0:
    p('do something')
my_list = ''
if len(my_list) > 0:
    p('do something')

def say_hello(name):
    if (name == 'world'):
        print('Enough of that now')
    else:
        print(f'Hello, {name}!')

say_hello('world')
say_hello('friend')   

number_of_apples = 1
if number_of_apples > 10:
    print('I have a lot of apples')
elif number_of_apples > 5:
    print('I have some apples')
elif number_of_apples == 1:
    print('I have an apple')
else:
    print('I have no apples')

birthday_is_today = True
number_of_items = 10
price = 10.00

if birthday_is_today:
    price = price * 0.85
if number_of_items > 5:
    price = price * 0.9

print(price)


def get_middle_char_or_none(var):
    print(len(var)) #5

    if len(var) % 2 == 0:
        return None
    else:
        return var[len(var)//2]

print(get_middle_char_or_none('abcefg'))

for number in [1, 2, 3, 4, 5]:
    print(number)

for character in 'foobar':
    print(character)   

number_list = [5, 15, 30, 50]
result = 0
for number in number_list:
    result += number # same as: result = result + number
print(result)

def find_strings_containing_a(strings):
    result = []
    for string in strings:
        if 'a' in string:
            result.append(string)
    return result

full_list = ['the mouse', 'some cats', 'a dog', 'people']
result = find_strings_containing_a(full_list)
print(result)

def find_strings_containing_a(strings):
    return [ string for string in strings if 'a' in string]

full_list = ['the mouse', 'some cats', 'a dog', 'an people']
result = find_strings_containing_a(full_list)
print(result)

def find_even_nums(nums):
    return [ num for num in nums if num %2==0]

full_list = [23,3,5,5476,567,3,45,24,3]
result = find_even_nums(full_list)
print(result)

#range range(start, stop, step)
for i in range(10, -10, -2):
    print(i)

def sum_cubes_to_n(n):
    result = 0
    for current in range(1, n + 1):
        print(f'iteration: {current} adding: {current**2} to current total: {result}')
        result += current**2
    return result
result = sum_cubes_to_n(5)
print(result)

x = 1
while x < 100:
    x = x * 2

print(x) 

#break exits the for loop completely. It “breaks out” of the loop.
#continue ends the current loop early and “continues” to the next one

for i in range(10):
    print(f'Start loop with i == {i}')
    if i == 3:
        print('Break out')
        break
    if i < 2:
        print(f'Continue')
        continue
    print('End loop')


#Each Python file is a module
#A folder is a package. If the folder contains files/subfolders, the package contains modules/subpackages.
#For your module (file) to access code from another, you must first import it
    #Each folder needs to contain a file called __init__.py in order to be a regular package rather than just a namespace. 
    #Namespaces can be spread over multiple folders in totally different locations. 
    #If in doubt, include the __init__.py file. The file can be left blank.

###    
#>>> os.chdir("/temp/devops/py/package")
#>>> os.chdir(r'c:\temp\devops\py\package')
#>>> os.chdir('c:\\temp\\devops\\py\\package')
#>>> print(os.getcwd())
#C:\temp\devops\py\package
### set PYTHONPATH=%PYTHONPATH%;C:\My_python_lib

#import example_module.bar
#from example_module import foo,bar # import * NOT recommended
#import example_module

import os
print(os.getcwd())

import math
print(f'{math.pi:.10f}')

import datetime
now = datetime.datetime.now()
print(now)
print(now.strftime('%d/%m/%y %H:%M'))
print(now.strftime('%y%m%d%H%M%S'))

#from package import module1 as my_mod1
#print(my_mod1.mod1var1)

# package management PyPi or privately owned repo
# pip  OR python3 -m pip
# pip install package-name  # optional version specifier >>>pip install package-name=1.0.0
# List your dependencies in a file and then install them with: pip install -r requirements.txt
# install poetry (better package/dependency manager: ps> (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py - )
#Sometimes you install packages that install their own dependencies in turn. Those nested dependencies that you aren’t accessing directly are the transitive dependencies

#poetry init #to add Poetry to a project. This only needs to be done once.
#poetry add package-name #to install a new package and automatically update your pyproject.toml and poetry.lock files as necessary. With just pip, you’d have to run multiple commands to achieve this.
#poetry install #to install everything that the current project needs (as specified by pyproject.toml).
#poetry show #to show your dependencies
#poetry run ... #to run a shell command using Poetry’s virtual environment for the current project. E.g. poetry run python will open up a REPL using the virtual environment’s copy of Python, so the correct packages should be installed. poetry run python my_app.py.

#class ~= type, class can be instantiated (instance), store data (attributes), and define functions to manipulate (methods)
from dog import Dog

#In Python, any class names you define should be in PascalCase, camelCase can have a lowercase first letter.
#my_dog = Dog()
#my_dog.name = 'Bob'
#print(f"My dog's name is {my_dog.name}")
#dog = Dog()
#print(f"My dog's name is {my_dog.name}")
from notification import Notification

from pantry import Pantry
initial_food_collection = {
    'grams of pasta': 500,
    'jars of jam': 2
}
my_pantry = Pantry(initial_food_collection)
print(f'{my_pantry.food_dictionary}')

my_pantry.print_contents()

initial_food_collection = {
    'grams of pasta': 500,
    'jars of jam': 2
}
my_pantry = Pantry(initial_food_collection)
my_pantry.print_contents()

my_pantry.add_food('potatoes', 3)
my_pantry.add_food('grams of pasta', 200)
my_pantry.print_contents()

from movingthing import MovingThing

my_list = [1,"Hello", True] #list item add methods
my_list.append(3)
my_list += [3]
print(my_list)

f = open("test.txt", mode = 'w')
f.write("my first file\n")
f.write("This file\n")
f.write("contains three lines\n")
f.close()

with open("test.txt",'r') as f: #auto close file tidier
    text_string = f.read()

print(text_string)

h_letters = [ letter for letter in 'human' ]
print(h_letters)

print ("CALC v2000!")
#oper = (input("Please enter operator (+-*/): "))
#num1 = int(input("Please enter 1st number: "))
#num2 = int(input("Please enter 2nd number: "))
#if oper == "+":
#    ans = num1 + num2
#elif oper == "-":
#    ans = num1 - num2
#elif oper == "*" or oper == "x":
#    ans = num1 * num2
#elif oper == "/":
#    ans = num1 / num2

#print("CALC v2000! says your answer is (drumroll): " {ans} )
#print( ans )

with open("calc.txt",'r') as f: #auto close file tidier
    #text_string = f.read().splitlines(True)
    text_string = [f.read().splitlines(True)]

#print (text_string)

text_string

for calc in text_string:
    #calc.split(" ") 

    #calc[1]

    oper = calc[1]
    num1 = calc[2]
    num2 = calc[3]

    if oper == "+":
        ans = num1 + num2
    elif oper == "-":
        ans = num1 - num2
    elif oper == "*" or oper == "x":
        ans = num1 * num2
    elif oper == "/":
        ans = num1 / num2
    #print (ans)

#file.read().splitlines()

from flask import Flask
app = Flask("demo")
@app.route("/hello")
def hello_world():
    return "Hello World!" 
#flask run
#127.0.0.1:5000/hello
