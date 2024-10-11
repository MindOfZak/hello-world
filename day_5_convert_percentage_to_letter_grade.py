#Read the percentage from the user
percentage = float(input("Enter the percentage: "))

#Determine the letter grade

if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
else:
    grade = 'F'

# Print the corresponding letter grade
print(f"The letter grade is: {grade}")

