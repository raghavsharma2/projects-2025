n = int(input("Enter a number (up to 50): "))
if n > 50:
    n = 50 

s= 0
print("Even numbers up to", n, ":")
for i in range(2, n + 1, 2): 
    print(i)
    s += i

print("Total of even numbers:", s)
