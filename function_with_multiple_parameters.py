def add(x,y) :
    return x + y

if __name__ == "__main__":
    result = add(3, 13)
    print(result)

def maximum(x, y):
    if x > y:
        return x
    else:
        return y

if __name__ == "__main__":
    result = maximum(3, 5)
    print(result)

# Function with No Return Value

def print_hello(name):
    print(f"Hello {name}")

if __name__ == "__main__":

    a = print_hello("Jimi")
    print(a)
