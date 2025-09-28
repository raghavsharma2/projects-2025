for i in range(1,5,1):
    for j in range(1,6):
        print(i,end="")
    print()
# reverse nested loop
for i in range(5,0,-1):
    for j in range(1,6):
        print(i,end="")
    print()
# continue statement
for i in range(1,6):
    if i == 3:
        continue
    print(i, end="")
# break statement
for i in range(1,6):
    if i == 3:
        break
    print(i, end="")