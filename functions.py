def multiply_five(number) :
    return number * 5

result_one = multiply_five(6) # call function with 10 and bind result
result_two = multiply_five(9)


print(result_one) # this prints the value of the result
print(result_two)

result_three = multiply_five(2) * multiply_five(3)
print(result_three)

def greater_than_five(x) :
    if x > 5:
        return True
    else:
        return False

if__name__ = "__main__":
    print(greather_than_five(3))
    print(greater_than_five(7))
    