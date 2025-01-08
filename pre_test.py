# Ranges can take either:

# an end value range(end)
# a start and end value range(start, end)
# a start, end, and step value range(start, end, step)

# By default start is 0 and step is 1.
# So range(10) is the same as both range(0,10) and range(0,10,1).

# Easy question 1 answered.
start = 3
end = 455

multiple = sum(range(start, end + 1))
total_sum = multiple * 42

print(multiple)
print(total_sum)

# Easy question 2 answered.

string = "Programminginpython"
total = 0 
for s in string:
    print(f"Adding the ascii code of {s} ({ord(s)}) to total")
    total = total + ord(s)
    
print(total)


# Medium Question 1 answered.

fib1 = 0
fib2 = 1

num_generated = 2

n = 10

while num_generated < n:
    #generate next fib number
    num_generated = num_generated + 1

print(num_generated)


























# apple_cost = 2
# banana_cost = 1.50

# customer_apple_total = apple_cost * 5 
# customer_banana_total = banana_cost * 8

# amount_paid = 20

# change = amount_paid - customer_apple_total - customer_banana_total

# print(f"The total cost for the customer is ${customer_banana_total + customer_apple_total}")
# if change >= 0:
#     print("The change to be returned is: $", change)
# else:
#     print("The customer still owes: $", abs(change))


# total_range = sum(range(0, 3 + 1))

# multiply = total_range * 4

# print(total_range)


# if total_range < 20:
#     print("total range is less than 20")
# elif total_range > 20:
#     print("total range is more than 20")

# if multiply < 20:
#     print("multiply is less than 20")
# elif multiply > 20:
#     print("multiply is more than 20")


# first_set_apples = 5
# second_set_apples = 8
# give_away = 3

# total_apples = first_set_apples + second_set_apples - give_away

# print(total_apples)

# orange_price = 3
# customer_bought = 7

# total_price = customer_bought * orange_price

# print(f"The total cost is ${total_price}")



# cost_per_apple = 2
# cost_per_banana = 1.50

# # Number of apples and bananas bought
# apples_bought = 5
# bananas_bought = 8

# # Calculate the total cost
# total_cost = (cost_per_apple * apples_bought) + (cost_per_banana * bananas_bought)

# # Amount paid by the customer
# amount_paid = 20

# # Calculate the change
# change = amount_paid - total_cost

# # Print the results
# print("The total cost is: $", total_cost)
# if change >= 0:
#     print("The change to be returned is: $", change)
# else:
#     print("The customer still owes: $", abs(change))