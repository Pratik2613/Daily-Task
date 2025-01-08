#1. Python program to check leap year

# Take year as input
year = int(input("Enter a year: "))

# Check if it's a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
------------------------------------------------------------------------------------------------------------------------------
#2. Python Program to Find the Largest Among Three Numbers

# Take three numbers as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the largest
largest = max(num1, num2, num3)

print(f"The largest number among {num1}, {num2}, and {num3} is {largest}.")

----------------------------------------------------------------------------------------------------------------------------------------
#3. Python Program to Check if a Number is Positive, Negative or 0

# Take a number as input
number = float(input("Enter a number: "))

# Check the sign of the number
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

-------------------------------------------------------------------------------------------------------------------------------------
#4. Atoy vendor supplies three types of toys: Battery Based Toys, Key-based
 Toys, and Electrical Charging Based Toys. The vendor gives a discount of
 10% on orders for battery-based toys if the order is for more than Rs. 1000.
 On orders of more than Rs. 100 for key-based toys, a discount of 5% is
 given, and a discount of 10% is given on orders for electrical charging based
 toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3
 are used for battery based toys, key-based toys, and electrical charging based
 toys respectively. Write a program that reads the product code and the order
 amount and prints out the net amount that the customer is required to pay
 after the discount.

# Take input for product code and order amount
product_code = int(input("Enter the product code (1 for Battery-based, 2 for Key-based, 3 for Electrical Charging-based): "))
order_amount = float(input("Enter the order amount: "))

# Initialize net amount
net_amount = order_amount

# Apply discounts based on product code and order amount
if product_code == 1:  # Battery-based toys
    if order_amount > 1000:
        net_amount = order_amount * 0.90  # 10% discount
elif product_code == 2:  # Key-based toys
    if order_amount > 100:
        net_amount = order_amount * 0.95  # 5% discount
elif product_code == 3:  # Electrical charging-based toys
    if order_amount > 500:
        net_amount = order_amount * 0.90  # 10% discount
else:
    print("Invalid product code!")

# Display the net amount
print(f"The net amount to be paid is Rs. {net_amount:.2f}")

--------------------------------------------------------------------------------------------------------------------------------------------

#5. A transport company charges fare according to the following table:

| **Distance (in km)** | **Charges (per km)** |
|-----------------------|----------------------|
| 1 - 50               | 8 Rs./km            |
| 51 - 100             | 10 Rs./km           |
| Above 100            | 12 Rs./km           |

# Take input for the distance traveled
distance = float(input("Enter the distance traveled (in km): "))

# Calculate the fare based on the distance
if 1 <= distance <= 50:
    fare = distance * 8  # 8 Rs./Km
elif 51 <= distance <= 100:
    fare = distance * 10  # 10 Rs./Km
elif distance > 100:
    fare = distance * 12  # 12 Rs./Km
else:
    fare = 0
    print("Invalid distance entered!")

# Display the fare
if fare > 0:
    print(f"The total fare for traveling {distance} km is Rs. {fare:.2f}.")




