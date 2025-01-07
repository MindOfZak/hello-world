def odd_test(x) :
    if x % 2 != 0:
        return True
    else:
        return False
if __name__ == "__main__":
    print(odd_test(3))
    print(odd_test(8))

# note: % is used to give the remainder of the division. If a number if divisible by 2 (i.e the remainder is 0) it is even; otherwise, it is odd.

