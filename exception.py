def divide_numbers(x, y):
    try:
        result = x / y
        print("Result:", result)
    except ZeroDivisionError:
        print("The division by zero operation is not allowed.")
numerator = 10
denominator = 0
a=10
b=20
divide_numbers(a, b)
def get_integer_input(enter):
    while True:
        try:
            value = int(input(enter))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")
n=get_integer_input("Enter an integer: ")
print("You entered:", n)
