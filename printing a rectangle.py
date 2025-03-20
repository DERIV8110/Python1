# Define dimensions
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Nested loop to print rectangle
for i in range(rows):  # Outer loop for rows
    for j in range(cols):  # Inner loop for columns
        print("*", end=" ")  # Print '*' and stay on the same line
    print()  # Move to the next line after each row
