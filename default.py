def msg():
    print("hi")
def add(a,b):
    print("a+b=", a + b)
def eligible(age=18):
    if(age>=18):
        print("Eligible")
    else:
        print("Not Eligible")
def area(side):
    return side * side
msg()
add(10, 20)
eligible(20)
print("Area of square with side =", area(5))