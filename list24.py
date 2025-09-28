l1 = {10,20,30,40,50}
for i in l1:
    print(i)
l2 = [4,6,9,12,15]
print(sorted(l2))
l3 = [1,2,3,4,5]
print(max(l3))

l4 = [1,2,3,4,5]
print(min(l4))

l5 = [1,4,8,9]
print(sum(l5))

l6 = [100,200,300]
if (300 in l6):
    print("true")
else:
    print("false")
numbers = [8,9,7,12,34,2,4,5,6,1]
even_numbers = []
odd_numbers = []
for num in numbers:
if(i%2==0):
    even_numbers.append(num)
else:
    odd_numbers.append(num)
print("Even numbers:", even_numbers)