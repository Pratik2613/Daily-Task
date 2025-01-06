# 1. Calculate the multiplication and sum of two numbers 

# Take input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate multiplication and sum
multiplication = num1 * num2
summation = num1 + num2

print(f"Multiplication: {multiplication}, Sum: {summation}")

------------------------------------------------------------------------------------------------------------------------
# 2. Declare two variables and print that which variable is largest using ternary operators

# Take input from user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Use ternary operator to find the largest
largest = a if a > b else b

print(f"The largest number is: {largest}")

------------------------------------------------------------------------------------------------------------------------
# 3. Python program to convert the temperature in degree centigrade to Fahrenheit 

# Take input from user
celsius = float(input("Enter the temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C is equal to {fahrenheit}°F")

-------------------------------------------------------------------------------------------------------------------------
# 4. Python program to find the area of a triangle whose sides are given

# Take input from the user
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

# Calculate the semi-perimeter
s = (a + b + c) / 2

# Calculate the area
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print(f"The area of the triangle is: {area:.2f}")
