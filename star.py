
#1. Take user input for the number of rows
rows = int(input("Enter the number of rows: "))

# Initialize the row counter
i = 1

# Generate the pattern
while i <= rows:  # Outer loop for rows
    # Print dashes
    j = rows - i  # Number of dashes decreases as rows progress
    while j > 0:
        print("-", end="")
        j -= 1
    
    # Print stars
    k = 0  # Number of stars increases as rows progress
    while k < i:
        print("*", end="")
        k += 1
    
    print()  # Move to the next row
    i += 1  # Increment the row counter

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2. Take user input for the number of rows
rows = int(input("Enter the number of rows: "))

# Initialize the row counter
i = 1

# Generate the pattern
while i <= rows:  # Outer loop for rows
    j = 1  # Inner loop counter for characters in the row
    while j <= i:  # Print characters for the current row
        if j % 2 == 1:  # Odd position: print 1
            print("1", end="")
        else:  # Even position: print 0
            print("0", end="")
        j += 1
    print()  # Move to the next row
    i += 1  # Increment the row counter

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#3. Take user input for the number of rows
rows = int(input("Enter the number of rows: "))

# Initialize the row counter
i = rows

# Generate the pattern
while i > 0:  # Outer loop for rows
    # Print dashes with spaces beside them
    spaces = rows - i
    while spaces > 0:
        print(" ", end="")  # Space added beside each dash
        spaces -= 1

    # Print numbers
    j = 1  # Inner loop for characters in the row
    while j <= i:
        if j % 2 == 1:  # Odd position: print 1
            print("1", end="")
        else:  # Even position: print 0
            print("0", end="")
        j += 1

    print()  # Move to the next row
    i -= 1  # Decrease the row counter
