# Program to calculate the area of a rectangle (decimal input)

# Prompt the user for length and width
length = float(input("Please enter the length of the rectangle (decimal): "))
width = float(input("Please enter the width of the rectangle (decimal): "))

# Calculate the area
area = length * width

# Print the result rounded to two decimal points
print(f"The area of the rectangle with length {length:.2f} and width {width:.2f} is {area:.2f}")