fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
fruits.remove("banana")
for fruit in fruits:
    print(fruit)
if "apple" in fruits:
    print("Apple is in the set")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)