def main():
    n = calculate(input("Please type an expression\n"))
    try:
        print (f"{n:.1f}")
    except TypeError:
        pass


def calculate(exp):
    x = float (exp.split()[0])
    y = float (exp.split()[2])
    operation = exp.split()[1]

    if operation == "+":
        return sum(x, y)
    if operation == "-":
        return subtract(x, y)
    if operation == "*":
        return multiply(x, y)
    if operation == "/":
        return devide(x, y)


def sum(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def devide(x, y):
    try:
         return x/y
    except ZeroDivisionError:
         print("division by zero!")



main()