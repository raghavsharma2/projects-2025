def cube(number):
    print(number ** 3)
num=int(input("Enter a number: "))
print("The cube of", num, "is:")
cube(5)

#program 2
def subjects(sub1,sub2,sub3):
    print("The subjects are:", sub1, sub2, sub3)
sub1 = input("Enter first subject: ")
sub2 = input("Enter second subject: ")
sub3 = input("Enter third subject: ")
print("The subjects are:")
avg = (sub1 + sub2 + sub3) / 3
subjects(sub1, sub2, sub3)