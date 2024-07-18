#this just print a certain index in an array of elements
lst = [1, 2, 3]
print(lst[2])
print(lst)
print(lst[0], "this prints index 0 which is [1]")

print("Good Morning")

#this snippet works with values that are positive 
#Value error
#ValueError: factorial() not defined for negative values

#import math
##print(math.factorial(num))

#this snippet will not work since its missing a library import math for it to work
#Name error
#Name Error if no import math
#num=int(input("Enter a number of whose factorial you want to find: "))
#print(math.factorial(num))

#calculating gcd
#num1=int(input("Enter a first number of whose gcd you want to find: "))
#num2=int(input("Enter a second number of whose gcd you want to find: "))
#print(math.gcd(num1,num2))


print("-----------------------------------------")
def getMonth(m):
    if m < 1 or m > 12:
        raise ValueError("Invalid")
    print(m)
getMonth(6)


#For print('x\97\x98')
print('x\97\x98')

print("----------------------------------------")

serialnumber=str(55555)
amount = float(44)

message = 'The serial number of the project is ', serialnumber, 'and it will cost', amount, '.' 
message_format = f'The serial number of the project is {serialnumber} and it will cost {amount}.' .format(serialnumber, amount) #format method
message_using_plus = 'The serial number of the project is'+ serialnumber + 'and it will cost'+str(amount)+'.' 

print(message, "- The message variable is a tuple of strings and numbers. When printed, it will display the tuple elements enclosed in parentheses.")
print(message_using_plus, "This concatenates the strings using the plus sign. Spaces need to be added manually, and numbers must be converted to strings to concatenate properly.")
print(message_format, " - This uses an f-string (formatted string literal) to embed the variables directly within the string. This is a concise and readable way to format strings.")

print("----------------------------------------")

loop_numbers = []

for i in range(10):
    loop_numbers.append(i)
    print(loop_numbers[i])
print(', '.join(map(str, loop_numbers)), "- This is printing an array of numbers from a loop")
    
print("----------------------------------------")
var_a = loop_numbers[::-1] #this prints the whole array in backwards
var_b = loop_numbers[::1] #prints th whole array
var_c = loop_numbers[1::1] #prints the whole array starting from 1
var_d = loop_numbers[:5] #prints the array starting from 0 to 4
var_e = loop_numbers[1:5] #prints the array starting from 0 to 4
# ::1 - printsthe whole array 
# ::-1 - prints the whole array but reverse
#1::1 - prints the whole array but starting from 1 hence (starting number index 1::)
#::5 - prints the whole array but stops at 4 hence (ending number index ::5)
print(var_a, "this is splice printing numbers backwards")
print(var_b, "this is splice printing numbers")
print(var_c, "this is splice printing numbers starting from 1 to 9")
print(var_d, "this is splice printing numbers starting from 0 to 4")
print(var_e, "this is splice printing numbers starting from 1 to 4")
print("----------------------------------------")
print("-----------------NEXT-------------------")
print("----------------------------------------")

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Slice to get the first 5 numbers
first_half = numbers[:5]
# Slice to get the last 5 numbers
second_half = numbers[5:]

print("Original list:", numbers)
print("First half:", first_half)
print("Second half:", second_half)

print("--------------------------------------")
# python program to demonstrate
# working of append function

# assign list
l = ['geeks']

# use method
l.append('for')
l.append('geeks')

# display list
print(l[0],l[1],l[2])
#or
print(l)

print("--------------------------------------")

animals = ["Bears", "Panthers", "Lions"] 
animals.append ("Jaguars")

for i in animals:
    print(i) #this wil print the array together with the new append string ,Lions, Jaguars
    
print("--------------------------------------")
animals.sort()
for i in animals:
    print(i) #this wil print the array together with the new append string that are sorted

print("--------------------------------------")
#bishop, king, knight, pawn , queen, rook

pieces = ["queen", "king" , "bishop", "pawn", "rook", "knight"]
pieces.sort()
print(pieces, "in a sorted maner")
print(pieces[::-1], "in a reverse sorted manner")
print(pieces[-1])
print(pieces[5])


print("--------------------------------------")
#Not, and, or

"""
x+y = 8 , x * y = 15, x-y = 2

8 > 7 = TRUE

and

15 < 15 = FALSE
= FALSE

or

2 > 2 = FALSE

 SUMMARY Z = FALSE


"""

s = 'abc'
for i in range (len(s)):
    print(s[i].upper())
    
print("--------------------------------------")

schedule = ["Opening Comments", "Breakfast", "Lunch", "Breakout Session", "End of the Day", "Opening Comments", "Goodbye"]
scheduled_event = 0
while(scheduled_event < len(schedule)):
    print(schedule[scheduled_event])
    scheduled_event += 1
    
    if schedule[scheduled_event] == "End of the Day":
        break
    else:
        continue
    
print("--------------------------------------")

def calcTotal(taxable, amount, salesTax, shipping):
    subtotal = 0  # Initialize subtotal variable
    
    if taxable == "Yes":
        subtotal = amount + (1 * salesTax) + shipping
    elif shipping == 0:
        pass
    else:
        subtotal = amount + shipping
    
    return subtotal

order1 = calcTotal("No", 500, 0.7, 0)
print("Your Order is", order1)

print("--------------------------------------")

import string
annualSales = 500000

if annualSales >= 700000:
    print("Great year")

elif annualSales >= 300000:
    print("Decent year")

else:
    print("Better luck next year")

print("Thank you for your efforts")

print(f"Your sales representative is Nicole, you are in the East region, "\
"and you are based in the Potomac office.")

print("--------------------------------------")

"""import unittest
a = 3
b = 6
class Test_Example_UnitTest (unittest.TestCase):
    def test_equal(self):
        self.assertEqual(2+8, a+b)
        
    if __name__ == '__main__':
        unittest.main() """
        
print("--------------------------------------")

"""loc = ["N", "S", "W", "E"]
response = input("Enter N, S, W, or E, for a location: ").upper()
while response not in loc:
    print ("Try Again")
    response = input("Enter N, S, W, E for a locaiton: ").upper()
    
print("You have selected", response)"""

print("--------------------------------------")

price = 9.95
items = 15

print(f"We have {items} items in stock")


print("--------------------------------------")

def test_memory(self):
    a = 3
    b = a
    
    self.asserIs(a,b)

print("--------------------------------------")
"""
try:
    x = float(input("Enter a number: "))
    y = float (input("Enter a number to divide by: "))
    
    print(f"The answer is {x/y}.")
except:
    print("Uoh Enter is wrong or divided by zero")
    
else:
    print ("Successfully played the game")
finally:
    print("Thank you for playing the game.")
"""

print("--------------------------------------")
"""
x = float(input("Enter a number: "))
y = float (input("Enter a number to divide by: "))

try:
    print(f"The answer is {x/y}")
except:
    if y == 0:
        raise Exception ("You Cannot divide by Zero")
finally:
    print("Thank you for playing the game")
 """
print("--------------------------------------")
import math
average_inventory = 77.4

upper_bound = math.ceil(average_inventory)
lower_bound = math.floor(average_inventory)
bound = math.trunc(average_inventory)

print(upper_bound, "what this does is removes the decimal and round it up")
print(lower_bound, "What this does is removes the decimal and does not round up nor down")
print(bound, "It just removes the decimals")

print("--------------------------------------")

import random

countries = ['USA', 'Canada', 'Mexico', 'Japan', 'Spain', 'Kenya']
a = random.choice(countries) #selects a round conuintry from the array
b = random.shuffle(countries) #prints an array of countries in a random manner
c = random.sample(countries, 2) #randomly selects 2 countries

print(f"\"{a}\"")
print(countries)
print(c)

print("--------------------------------------")

"""
io.open() - is the preferred, higher-level interface to file I/O. It wraps the OS-level file descriptor in an object that you can use to access the file in a Pythonic manner.

math.ceil() -  function, part of Python's math module, is used for rounding a number up to the nearest integer. This function is particularly useful when you need an integer greater than or equal to a given number. 

os.mkdir() - All functions in the OS module raise OSError in the case of invalid or inaccessible file names and paths, or other arguments that have the correct type, but are not accepted by the operating system.

sys.exit() - These commands halt the program or interpreter, allowing the user to gracefully terminate the execution.
"""

print("--------------------------------------")
import math
pi = math.pi

radius = float(input("Enter radius of a circle: "))
area = pi*radius**2

print(f"A circle with a radius of {radius} will have an area of %.2f." %area)

#%.2f. - what this does is 2 decimal places
print("--------------------------------------")

import datetime

log_time = datetime.datetime.now()
print(f"Entry time now is {log_time}")

# Here are the separated ones
current_time = datetime.datetime.now().time() #returns the time
current_date = datetime.date.today() #returns the date
seconds = current_time.second #returns the seconds
#day = datetime.date.weekday()
date_obj = datetime.datetime.strftime

print(f"Time now is {current_time}, and the date is {current_date}, with {seconds} seconds")
print(f"Time now for date_ob is {date_obj}")
#print(f"current day is: {day}")


print("--------------------------------------")
print("--------------------------------------")
print("--------------------------------------")
print("--------------------------------------")

cities = ['Anchorage', 'Juneau', 'Fairbank', 'Ketchikan', 'Sitka', 'Wasilla']
for city in cities: 
    print(f'{city} is a famouse Alakaskan city.')
    if city == 'Ketchikan':
        break
print("--------------------------------------")
print("--------------------------------------")

""" a = 2
print (a)
b = 3
a**=b
#
#so what it does is that 2**3 = 8 and 
#8//3 = 2
print(a)
print(b)
a//=b
print(a) #answer will be 2 """
print("--------------------------------------")
a = 5
b = 2
c = 3
a**=b
b*=c
a//=b

print(a)
print(b)
print(c)

"""
TRUE AND TRUE = TRUE
TRUE AND FALSE = FALSE
FALSE AND TRUE = FALSE
FALSE AND FALSE = FALSE

TRUE OR FALSE = TRUE
TRUE OR TRUE = TRUE
FALSE OR TRUE = TRUE
FALSE OR FALSE = FALSE

NOT TRUE = FALSE
NOT FALSE = TRUE


"""
print("--------------------------------------")

""" from random import randint
for i in range (5):
    guess = int(input("Enter a number from 1 to 10: "))
    randNum = randint(1,10)
    
    if guess == randNum:
        print("We matched!")
        break
    else:
        print("We did not match sorry, try again") """

print("--------------------------------------")
print("--------------------------------------")
print("--------------------------------------")
print("--------------------------------------")

classday = ['Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat']
student = []
for day in classday:
    print(f"Day: {day}")
    for student in range(1, 11):
        print(f"student {student}")

print("--------------------------------------")




# Assuming the intention is to print activities for a 30-day program
for dailyProgram in range(1, 31):  # Loop from day 1 to day 30
    if dailyProgram == 15:
        print("No activity for on day 15")  # Special case for day 15
        continue  # Skip the rest of the loop for day 15
    print(f"This is your activity for day {dailyProgram}")  # Print activity for each day


print("--------------------------------------")

import random

for i in range(10):
    print(random.randrange(3,102,3))
    print(random.random())

print ("--------------------------------------")

import math
a = -14

print(math.fabs(a))

print ("--------------------------------------")

import math

a = float("nan") #not a real number
b = float(33)
c = math.isnan(a)
d = math.isnan(b)

print(a)
print(b)
print(c)
print(d)

print("--------------------------------------")

attendance = [300, 250, 200, 400, 150, 225, 325]

print(max(attendance))
print(min(attendance))

print("--------------------------------------")

name = input("what is your name: ")
print(name)   

print("--------------------------------------")

x = 4
while x >= 1:
    if x%4 == 0:
        print("Party")
    elif x-2 < 0:
        print("Cake")
    elif x/3 == 0:
        print("Greeting")
    else:
        print("Birthday")
    x = x -1 

print("--------------------------------------")

# Create an empty list to store colors
colors = []

# Loop through the range 0 to 199
for i in range(200):
    # Append each number to the colors list (assuming you want to store the numbers)
    colors.append(i)

# Print every second number in the colors list starting from the first index
print(colors[1::2])
print("--------------------------------------") 

# Start an infinite loop
while True:
    try:
        # Prompt the user to enter their age and convert it to an integer
        age = int(input("Enter your age: "))
        
        # Prompt the user to enter a four-digit year and convert it to an integer
        year = int(input("Enter your four digit year: "))
        
        # Calculate the year of birth by subtracting the age from the year
        born = year - age
        
        # Print the calculated year of birth
        print(f"You were born in {born}")
        
        # Exit the loop after successful input and calculation
        break
    
    # Catch ValueError in case of invalid input (non-integer values)
    except ValueError:
        # Inform the user about the invalid input and prompt again
        print("Invalid input. Please enter a valid age and year.")
print("--------------------------------------") 

import math  # Import the math module for mathematical operations

# Initialize total deposit amount and number of customers
total_depo = 129
num_cust = 21

# Calculate the average balance using different methods
average_bal = int(total_depo // num_cust)  # Integer division and convert to integer
average_bal2 = total_depo // num_cust  # Integer division
average_bal3 = math.trunc(total_depo // num_cust)  # Truncate the result of integer division
average_bal4 = math.frexp(total_depo / num_cust)  # Return the mantissa and exponent of total_depo//num_cust
average_bal5 = total_depo / num_cust  # Floating-point division

# Print the results of the different average balance calculations
print(f"{average_bal} average bal 1")
print(f"{average_bal2} average bal 2")
print(f"{average_bal3} NO average bal 3")
print(f"{average_bal4} NO average bal 4")
print(f"{average_bal5} NO average bal 5")


print("--------------------------------------")

item = input("Enter the item name: ")
sales = input ("Enter the Quantity: ")

print(f"{item} is the item name and, {sales} is the quantity")
print('"{0}",{1}'. format(item,sales))
print("{0},{1}".format(item,sales))
print('"%s",%s'%(item,sales))