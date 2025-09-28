a = 0   # a = score
b = 1   # b = marks for correct answer

print("Welcome to the Python Quiz!")
print("Answer the following questions:\n")

# Question 1
print("1. What is the capital of India?")
print("a) Mumbai")
print("b) Delhi")
print("c) Kolkata")
answer = input("Enter your choice (a/b/c): ")

if answer == "a":
    print("Wrong!")
elif answer == "b":
    print("Correct!")
    a = a + b
elif answer == "c":
    print("Wrong!")
else:
    print("Invalid choice!")

# Question 2
print("\n2. Which planet is known as the Red Planet?")
print("a) Earth")
print("b) Mars")
print("c) Venus")
answer = input("Enter your choice (a/b/c): ")

if answer == "a":
    print("Wrong!")
elif answer == "b":
    print("Correct!")
    a = a + b
elif answer == "c":
    print("Wrong!")
else:
    print("Invalid choice!")

# Question 3
print("\n3. Who wrote the National Anthem of India?")
print("a) Rabindranath Tagore")
print("b) Mahatma Gandhi")
print("c) Subhas Chandra Bose")
answer = input("Enter your choice (a/b/c): ")

if answer == "a":
    print("Correct!")
    a = a + b
elif answer == "b":
    print("Wrong!")
elif answer == "c":
    print("Wrong!")
else:
    print("Invalid choice!")

# Question 4
print("\n4. What is the largest ocean in the world?")
print("a) Atlantic Ocean")
print("b) Pacific Ocean")
print("c) Indian Ocean")
answer = input("Enter your choice (a/b/c): ")

if answer == "a":
    print("Wrong!")
elif answer == "b":
    print("Correct!")
    a = a + b
elif answer == "c":
    print("Wrong!")
else:
    print("Invalid choice!")

# Question 5
print("\n5. Which language is this quiz written in?")
print("a) C++")
print("b) Python")
print("c) Java")
answer = input("Enter your choice (a/b/c): ")

if answer == "a":
    print("Wrong!")
elif answer == "b":
    print("Correct!")
    a = a + b
elif answer == "c":
    print("Wrong!")
else:
    print("Invalid choice!")

# Final Score
print("\nYour final score is:", a, "out of 5")