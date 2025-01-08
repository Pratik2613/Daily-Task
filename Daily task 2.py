#1. Using input() function take one number from the user and using ternary operators
check whether the number is even or odd

# Take a number as input
number = int(input("Enter a number: "))

# Check if it's even or odd using a ternary operator
result = "Even"
if number % 2 == 0
else "Odd"

print(f"The number {number} is {result}.")
----------------------------------------------------------------------------------------------------------------------------
#2. Using input function take two number and then swap the number

# Take two numbers as input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"Before swapping: num1 = {num1}, num2 = {num2}")

# Swap the numbers
num1, num2 = num2, num1

print(f"After swapping: num1 = {num1}, num2 = {num2}")

----------------------------------------------------------------------------------------------------------------------------
#3. Write a Program to Convert Kilometers to Miles

# Take the distance in kilometers as input
kilometers = float(input("Enter distance in kilometers: "))

# Conversion factor
conversion_factor = 0.621371

# Convert to miles
miles = kilometers * conversion_factor

print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")

----------------------------------------------------------------------------------------------------------------------------
#4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year.     

# Take input values for principal, rate, and time
principal = float(input("Enter the principal amount (Rs.): "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the time (years): "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

print(f"The Simple Interest on Rs. {principal} for {time} years at {rate}% is Rs. {simple_interest:.2f}.")
                       